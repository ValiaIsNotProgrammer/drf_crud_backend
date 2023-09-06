from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from authentication.jwt_authentication import CustomJWTAuthentication
from .models import OTP
from .serializers import OTPSerializer


class OTPView(ModelViewSet):
    name = 'otp'
    queryset = OTP.objects.all()
    serializer_class = OTPSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user = request.user
        code = request.data.get('code')

        if code == user.otp.code:
            return Response({"message": "The code is correct."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "The code is incorrect"}, status=status.HTTP_400_BAD_REQUEST)







