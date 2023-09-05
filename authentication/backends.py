from django.contrib.auth.backends import ModelBackend
from django.db.models import QuerySet

from profile.models import CustomProfileModel


class AuthenticationBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            profile = CustomProfileModel.objects.get(email=email)
            if profile.check_password(password):
                return profile
        except CustomProfileModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomProfileModel.objects.get(pk=user_id)
        except CustomProfileModel.DoesNotExist:
            return None



        
