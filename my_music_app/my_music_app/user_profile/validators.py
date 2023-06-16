from django.core import exceptions


def user_name_validator(value):
    for char in value:
        if not char.isalnum() and char != '_':
            raise exceptions.ValidationError('Ensure this value contains only letters, numbers, and underscore.')
