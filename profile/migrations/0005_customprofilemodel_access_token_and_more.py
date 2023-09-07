# Generated by Django 4.2.4 on 2023-09-05 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0004_customprofilemodel_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='customprofilemodel',
            name='access_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customprofilemodel',
            name='refresh_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]