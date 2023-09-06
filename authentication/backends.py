from django.contrib.auth.backends import ModelBackend

from authentication.utils import generate_jwt_data, save_jwt_data
from profile.models import CustomProfileModel


class AuthenticationBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = CustomProfileModel.objects.get(email=email)
            access_token, refresh_token = generate_jwt_data(user)
            save_jwt_data(access_token, refresh_token, user)
            if user.check_password(password):
                return user
        except CustomProfileModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomProfileModel.objects.get(pk=user_id)
        except CustomProfileModel.DoesNotExist:
            return None



        
