# Generated by Django 4.2.4 on 2023-09-04 20:01

import common_validators.fields_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_remove_customprofilemodel_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customprofilemodel',
            name='password',
            field=models.CharField(max_length=100, validators=[common_validators.fields_validators.CustomPasswordValidator]),
        ),
    ]
