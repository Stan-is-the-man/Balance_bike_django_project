from django.core.exceptions import ValidationError


def name_has_only_letters(name):
    for char in name:
        if not char.isalpha():
            raise ValidationError('Името трябва да съдържа само букви')
