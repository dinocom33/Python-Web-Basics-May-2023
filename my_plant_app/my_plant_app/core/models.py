from django.core import validators
from django.db import models

from .validators import validate_first_and_last__name, plant_name_validator


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(2),
        )
    )

    first_name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=(
            validate_first_and_last__name,
        )
    )

    last_name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=(
            validate_first_and_last__name,
        )
    )

    profile_image_url = models.URLField(
        null=True,
        blank=True,
    )

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.username


class Plant(models.Model):
    OUTDOOR_PLANTS = 'Outdoor Plants'
    INDOOR_PLANTS = 'Indoor Plants'
    CHOICES = (
        (OUTDOOR_PLANTS, OUTDOOR_PLANTS),
        (INDOOR_PLANTS, INDOOR_PLANTS)
    )

    plant_type = models.CharField(
        max_length=14,
        null=False,
        blank=False,
        choices=CHOICES,
    )

    plant_name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(2),
            plant_name_validator,
        )
    )

    plant_image_url = models.URLField(
        null=False,
        blank=False,
    )

    plant_description = models.TextField(
        null=False,
        blank=False,
    )

    price = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.plant_name
