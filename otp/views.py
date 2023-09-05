from rest_framework import status
from rest_framework.decorators import action, authentication_classes
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import OTP
from .serializers import OTPSerializer
from django.contrib.auth import authenticate, login
from rest_framework.exceptions import AuthenticationFailed


class OTPView(ModelViewSet):
    name = 'otpview'
    queryset = OTP.objects.all()
    serializer_class = OTPSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     if not serializer.is_valid():
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     return Response({"o":"okey"})




    @action(detail=False, methods=['post', 'get'], url_path='verification')
    @authentication_classes([JWTAuthentication])
    def verification(self, request):
        if request.method == "get":
            return Response({"message": "Письмо отправлено"})
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"o":"okey"})




