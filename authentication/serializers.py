from rest_framework import serializers
from django.contrib.auth import authenticate
from common_validators.json_validator import JSONValidator
from common_validators.fields_validators import CustomEmailValidator, CustomPasswordValidator


class AuthenticationSerializer(serializers.Serializer):

    email = serializers.EmailField(validators=[CustomEmailValidator])
    password = serializers.CharField(write_only=True, validators=[CustomPasswordValidator])

    class Meta:
        fields = "__all__"
        USERNAME_FIELD = "email"
        validators = [
            JSONValidator,
        ]