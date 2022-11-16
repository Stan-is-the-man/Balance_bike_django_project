from django.core.validators import MinValueValidator, MinLengthValidator, RegexValidator
from django.db import models

from additionals.choices import EdgeColorChoices
from additionals.validators import name_has_only_letters


class BalanceBike(models.Model):
    COLOR_MAX_LEN = 15
    NAME_MAX_LEN = 20
    PRICE_MIN_VALUE = 150

    model = models.CharField(
        max_length=NAME_MAX_LEN
    )

    color = models.CharField(
        choices=EdgeColorChoices.choices,
        max_length=COLOR_MAX_LEN,
    )

    price = models.PositiveIntegerField(
        validators=[
            MinValueValidator(PRICE_MIN_VALUE),
        ]
    )

    image = models.ImageField(
        upload_to='static/images'
    )

    custom_tag = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return self.color


class Customer(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 20
    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 20
    CITY_MIN_LEN = 2
    CITY_MAX_LEN = 20
    ADDRESS_MAX_LEN = 40

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=[
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            name_has_only_letters,
        ]
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LEN),
            name_has_only_letters,
        ]
    )

    email = models.EmailField(unique=True,)

    phone = models.IntegerField(
        validators=[
            RegexValidator(regex='^.{10}$', message='Телефонния номер трябва да съдържа точно 10 цифри', code='nomatch')
        ]
    )

    city = models.CharField(
        max_length=CITY_MAX_LEN,
        validators=[MinLengthValidator(CITY_MIN_LEN), ]
    )

    address = models.TextField(max_length=ADDRESS_MAX_LEN)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
