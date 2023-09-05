# from django.db import models
# from common_validators.fields_validators import \
#     CustomNameValidator, CustomPasswordValidator, CustomEmailValidator


# class Authorization(models.Model):
#
#     name = models.CharField(max_length=50, validators=[CustomNameValidator])
#     email = models.EmailField(max_length=100, unique=True, validators=[CustomEmailValidator])
#     password = models.CharField(max_length=50, validators=[CustomPasswordValidator])
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name_plural = "Users"



