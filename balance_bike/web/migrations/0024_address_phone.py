# Generated by Django 4.1.3 on 2022-11-28 08:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0023_address_first_name_address_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='phone',
            field=models.CharField(default=1111111111, max_length=10, validators=[django.core.validators.MinLengthValidator(10)]),
            preserve_default=False,
        ),
    ]
