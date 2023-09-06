from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authentication.jwt_authentication import CustomJWTAuthentication
from .models import CustomProfileModel
from .serializers import ProfileSerializer


class ProfileView(RetrieveUpdateDestroyAPIView):

    name = "profile"
    lookup_field = "email"
    queryset = CustomProfileModel.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomJWTAuthentication]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        user = request.user
        return Response({"message": "Profile updated successfully", "email": user.email, "user_id": user.id},
                        status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        user = request.user
        return Response({"message": "Profile updated partially", "email": user.email, "user_id": user.id},
                        status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        return Response({"message": "Profile deleted successfully", "email": user.email, "user_id": user.id},
                        status=status.HTTP_200_OK)








