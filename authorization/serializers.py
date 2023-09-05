from rest_framework import serializers
from profile.models import CustomProfileModel
from common_validators.json_validator import JSONValidator


class AuthorizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomProfileModel
        fields = ["username", "email", "password"]
        validators = [
            JSONValidator
        ]

