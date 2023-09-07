# Generated by Django 4.2.4 on 2023-09-05 17:01

import common_validators.fields_validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6, validators=[common_validators.fields_validators.CustomOTPValidator])),
                ('secret', models.CharField(max_length=32, validators=[common_validators.fields_validators.CustomSecretValidator])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='otp_codes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': "OTP's",
            },
        ),
    ]