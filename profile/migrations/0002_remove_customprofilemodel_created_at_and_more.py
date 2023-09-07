# Generated by Django 4.2.4 on 2023-09-04 18:09

import common_validators.fields_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customprofilemodel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='customprofilemodel',
            name='name',
        ),
        migrations.RemoveField(
            model_name='customprofilemodel',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='customprofilemodel',
            name='username',
            field=models.CharField(max_length=50, validators=[common_validators.fields_validators.CustomNameValidator]),
        ),
    ]
