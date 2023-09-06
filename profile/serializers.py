from rest_framework import serializers
from .models import CustomProfileModel
from common_validators.json_validator import JSONValidator


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomProfileModel
        fields = ["email", "username", "password", "access_token", "refresh_token", "otp"]
        validators = [
            JSONValidator
        ]
