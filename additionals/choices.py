from django.db import models


class EdgeColorChoices(models.TextChoices):
    BROWN = 'Кафяв'
    BLUE = 'Син'
    PINK = 'Розов'


class ModelChoices(models.TextChoices):
    CLASSIC = 'Класик'
    FUTURE_MODELS = 'Бъдещ модел'


class StatusChoices(models.TextChoices):
    PENDING = 'Обработва се'
    SENT = 'Изпратена'
    DELIVERED = 'Доставена'
    CANCELED = 'Отказана'
