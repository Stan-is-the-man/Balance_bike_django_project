from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from additionals.choices import EdgeColorChoices, ModelChoices, StatusChoices
from additionals.validators import name_has_only_letters, number_has_only_digits


class BalanceBike(models.Model):
    MODEL_MAX_LEN = 15
    COLOR_MAX_LEN = 15
    NAME_MAX_LEN = 20
    PRICE_MIN_VALUE = 179

    # just classic model for now
    model = models.CharField(
        choices=ModelChoices.choices,
        max_length=MODEL_MAX_LEN,
        verbose_name='Модел'
    )

    # 3 available choices for now
    color = models.CharField(
        choices=EdgeColorChoices.choices,
        max_length=COLOR_MAX_LEN,
        verbose_name='Цвят'

    )

    price = models.FloatField(
        verbose_name='Цена',
        validators=[
            MinValueValidator(PRICE_MIN_VALUE),
        ]
    )

    image = models.ImageField(
        verbose_name='Снимка',
        upload_to='static/images'
    )

    quantity_available = models.IntegerField(
        default=1,
        verbose_name='Налично количество на склад')

    def __str__(self):
        return f"Колело за баланс - {self.color} цвят"

    def bike_name(self):
        return f"Колело за баланс - {self.color} цвят"


class Customer(AbstractUser):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 20
    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 20
    PHONE_MIN_LEN = 10

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=[
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            name_has_only_letters,
        ],
        verbose_name="Име",
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LEN),
            name_has_only_letters,

        ],
        verbose_name="Фамилия",
    )

    email = models.EmailField(
        unique=True,
        verbose_name="Имейл",
    )

    phone = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(PHONE_MIN_LEN),
            number_has_only_digits,
        ],
        verbose_name="Телефон",
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Address(models.Model):
    NAME_FOR_ENGRAVING = 20
    PHONE_MIN_LEN = 10

    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 20
    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 20

    user = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    city = models.CharField(
        max_length=150,
        verbose_name="Населено място",
    )

    street = models.CharField(
        max_length=50,
        verbose_name="Адрес",
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        verbose_name="Име",
        validators=[
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            name_has_only_letters,

        ]
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        verbose_name="Фамилия",
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LEN),
            name_has_only_letters,
        ]
    )

    phone = models.CharField(
        max_length=10,
        verbose_name="Телефон",
        validators=[
            MinLengthValidator(PHONE_MIN_LEN),
            number_has_only_digits,
        ],
    )

    name_for_engraving = models.CharField(
        blank=True,
        null=True,
        max_length=NAME_FOR_ENGRAVING,
        verbose_name="Име За Гравиране",
    )

    def __str__(self):
        return self.city


class Cart(models.Model):
    user = models.ForeignKey(
        Customer,
        verbose_name="Потребителско име",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        BalanceBike,
        verbose_name="Продукт",
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name="Количество"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата на създаване"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Последно променена"
    )

    def __str__(self):
        return str(self.user)

    @property
    def total_price(self):
        return self.quantity * self.product.price


class Order(models.Model):
    STATUS_MAX_LEN = 20

    user = models.ForeignKey(
        Customer,
        verbose_name="Потребител",
        on_delete=models.CASCADE
    )
    address = models.ForeignKey(
        Address,
        verbose_name="Адрес за доставка",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        BalanceBike,
        verbose_name="Продукт",
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Количество"
    )
    ordered_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата на поръчка"
    )
    status = models.CharField(
        default="Обработва се",
        choices=StatusChoices.choices,
        max_length=STATUS_MAX_LEN,
        verbose_name='Статус на поръчка',
    )
