from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from profile.models import CustomProfileModel
from .serializers import AuthenticationSerializer
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.urls import reverse
from otp.utils import send_otp_mail, save_otp_data, generate_otp_data, prepare_text_mail


class AuthenticationView(ModelViewSet):
    name = "authentication"
    queryset = CustomProfileModel.objects.all()
    serializer_class = AuthenticationSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return self.authenticate_user(serializer, request)

    def authenticate_user(self, serializer, request):

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        headers = self.get_success_headers(serializer.data)

        user = authenticate(request, email=email, password=password)

        if user:
            secret, otp_code, kwargs = self.prepare_send_mail(email)
            save_otp_data(otp_code, secret, user)
            access_token, refresh_token = self.generate_jwt(user)
            return self.send_mail(**kwargs)

        return Response({"message": "User is not exist"}, status=status.HTTP_404_NOT_FOUND, headers=headers)


    def generate_jwt(self, user):
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        return access_token, refresh_token

    def save_jwt(self, user):
        user.profile.access_token = access_token
        user.profile.refresh_token = refresh_token
        user.profile.save()
    def send_mail(self, *args, **kwargs):
        try:
            send_otp_mail(**kwargs)
        except Exception as e:
            print(f"Email sending failed: {str(e)}")
            return Response({"message": "Email sending failed", "error": str(e)})
        otp_verification_url = reverse('otpview-verification')
        # return Response({"message": "Письмо отправлено",
        #                 "otp_verification_url": otp_verification_url})
        return redirect(otp_verification_url)



    def prepare_send_mail(self, email: str) -> tuple:
        secret, otp_code = generate_otp_data()
        kwargs = prepare_text_mail(email, otp_code)
        return secret, otp_code, kwargs


    def get_response_from_data(self, data: dict, headers):

        if "error" in data.keys():
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR, headers=headers)

        return Response(data, status=status.HTTP_202_ACCEPTED, headers=headers)
