from django.core import exceptions


def validate_only_alpha(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Ensure this value contains only letters.')


def file_size_validator(image):
    filesize = image.file.size
    megabyte_limits = 5.0
    if filesize > megabyte_limits * 1024 * 1024:
        raise exceptions.ValidationError(f'Max file size is {megabyte_limits}MB')
