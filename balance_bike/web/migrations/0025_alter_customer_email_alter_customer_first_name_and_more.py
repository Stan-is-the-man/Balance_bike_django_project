# Generated by Django 4.1.3 on 2022-12-01 07:55

import additionals.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0024_address_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Имейл'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), additionals.validators.name_has_only_letters], verbose_name='Име'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), additionals.validators.name_has_only_letters], verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Телефон'),
        ),
    ]