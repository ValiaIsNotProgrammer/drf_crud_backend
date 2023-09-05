from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework import status
from .serializers import AuthorizationSerializer


class CreateAuthorizationView(CreateAPIView):
    name = "authorization"
    serializer_class = AuthorizationSerializer

    # TODO: выдать токен обновления и токен доступа (или JWS)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED, headers=headers)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)  # hash password
        instance.save()


