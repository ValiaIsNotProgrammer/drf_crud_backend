from django.db import models

from common_validators.fields_validators import CustomOTPValidator, CustomSecretValidator
from profile.models import CustomProfileModel


class OTP(models.Model):
    code = models.CharField(max_length=6, validators=[CustomOTPValidator])
    secret = models.CharField(max_length=32, validators=[CustomSecretValidator])
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(blank=False, default=True)
    profile = models.ForeignKey("profile.CustomProfileModel", on_delete=models.CASCADE, related_name='otp_codes')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name_plural = "OTP's"
