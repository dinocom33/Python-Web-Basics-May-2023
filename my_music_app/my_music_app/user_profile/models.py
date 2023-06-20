from django.core import validators
from django.db import models

from .validators import user_name_validator


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(2),
            user_name_validator,
        ),
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            validators.MinValueValidator(0),
        ]
    )
