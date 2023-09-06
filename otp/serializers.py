from rest_framework import serializers

from common_validators.json_validator import JSONValidator
from .models import OTP


class OTPSerializer(serializers.ModelSerializer):

    class Meta:
        model = OTP
        fields = ["code"]
        validators = [
            JSONValidator
        ]