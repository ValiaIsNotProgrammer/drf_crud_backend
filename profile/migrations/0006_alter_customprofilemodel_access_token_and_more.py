# Generated by Django 4.2.4 on 2023-09-06 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0005_customprofilemodel_access_token_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customprofilemodel',
            name='access_token',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='customprofilemodel',
            name='refresh_token',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]