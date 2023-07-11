from django.core.exceptions import ValidationError


def first_and_last_name_validator(value):
    if not value[0].isalpha():
        raise ValidationError('Your name must start with a letter!')


def fruit_name_validator(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError('Fruit name should contain only letters!')
