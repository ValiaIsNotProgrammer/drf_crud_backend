from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Model
from common_validators.fields_validators import \
    CustomNameValidator, CustomPasswordValidator, CustomEmailValidator


class CustomProfileModel(AbstractUser):

    username = models.CharField(max_length=50, unique=False, validators=[CustomNameValidator])
    email = models.EmailField(max_length=100, unique=True, validators=[CustomEmailValidator])
    password = models.CharField(max_length=100, validators=[CustomPasswordValidator])
    otp = models.ForeignKey("otp.OTP", on_delete=models.CASCADE, null=True)
    access_token = models.CharField(max_length=300, blank=True, null=True)
    refresh_token = models.CharField(max_length=300, blank=True, null=True)

    USERNAME_FIELD = 'email'  # make field "email" as id
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Users"


