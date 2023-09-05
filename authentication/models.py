from django.db import models
from common_validators.fields_validators import \
    CustomEmailValidator, CustomPasswordValidator, CustomOTPValidator


class Authentication(models.Model):
    email = models.EmailField(max_length=100, validators=[CustomEmailValidator])
    password = models.CharField(max_length=50, validators=[CustomPasswordValidator])

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Authentications"
