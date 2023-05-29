from django.core.exceptions import ValidationError

def file_size_validator(image):
    filesize = image.file.size
    megabyte_limits = 5.0
    if filesize > megabyte_limits * 1024 * 1024:
        raise ValidationError(f'Max file size is {megabyte_limits}MB')



