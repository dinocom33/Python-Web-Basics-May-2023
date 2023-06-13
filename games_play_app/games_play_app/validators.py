from django.core.exceptions import ValidationError


def rating_validator(value):
    if not 1.0 <= value <= 5.0:
        raise ValidationError('Rating must be between 1.0 and 5.0')
