from django.core import validators
from django.db import models

from fruitipedia_app.web.validators import first_and_last_name_validator, fruit_name_validator


class ProfileModel(models.Model):
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=25,
        validators=(
            validators.MinLengthValidator(2),
            first_and_last_name_validator,
        )
    )
    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=35,
        validators=(
            validators.MinLengthValidator(1),
            first_and_last_name_validator,
        )
    )

    email = models.EmailField(
        null=False,
        blank=False,
        max_length=40,
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(
            validators.MinLengthValidator(8),
        )
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    age = models.IntegerField(
        default=18,
        null=True,
        blank=True,
    )

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class FruitModel(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=(
            validators.MinLengthValidator(2),
            fruit_name_validator,
        )
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
