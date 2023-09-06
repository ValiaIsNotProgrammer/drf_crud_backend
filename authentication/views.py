from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate

from profile.models import CustomProfileModel
from .serializers import AuthenticationSerializer
from otp.utils import send_otp_mail, save_otp_data, generate_mail_data


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

    def authenticate_user(self, serializer, request) -> Response:

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]
        headers = self.get_success_headers(serializer.data)
        user = authenticate(request, email=email, password=password)

        if not user:
            return Response({"message": "User is not exist"}, status=status.HTTP_404_NOT_FOUND, headers=headers)

        secret, otp_code, kwargs = generate_mail_data(email)
        save_otp_data(otp_code, secret, user)

        try:
            return self.send_mail(user, **kwargs)

        except Exception:
            # print(f"Email sending failed: {str(e)}")
            return Response({"message": "Email sending failed"})

    def send_mail(self, user, *args, **kwargs) -> Response:
        send_otp_mail(**kwargs)
        return Response({"message": "OTP code has been sent to your email",
                         "access token": user.access_token,
                         "refresh token": user.refresh_token})

