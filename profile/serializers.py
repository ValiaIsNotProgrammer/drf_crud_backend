from rest_framework import serializers
from .models import CustomProfileModel
from common_validators.json_validator import JSONValidator


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomProfileModel
        fields = "__all__"
        validators = [
            JSONValidator
        ]
