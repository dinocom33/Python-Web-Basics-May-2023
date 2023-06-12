from django.core.exceptions import ValidationError


def validate_first_and_last__name(value):
    if not value[0].upper():
        raise ValidationError('Your name must start with a capital letter!')


def plant_name_validator(value):
    if not value.isalpha():
        raise ValidationError('Plant name should contain only letters!')
