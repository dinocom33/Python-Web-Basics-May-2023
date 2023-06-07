from django.core import validators
from django.db import models

from car_collection.web.validators import valid_year_validator


class Profile(models.Model):
    username = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        validators=[validators.MinLengthValidator(2, 'The username must be a minimum of 2 chars')]
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(18),
        )
    )

    password = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name='Last Name',
    )

    image = models.ImageField(
        null=True,
        blank=True,
        verbose_name='Profile Picture',
    )

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Car(models.Model):
    SPORTS_CAR = 'Sports Car'
    PICKUP_CAR = 'Pickup'
    CROSSOVER_CAR = 'Crossover'
    MINIBUS_CAR = 'Minibus'
    OTHER = 'Other'

    CHOICES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP_CAR, PICKUP_CAR),
        (CROSSOVER_CAR, CROSSOVER_CAR),
        (MINIBUS_CAR, MINIBUS_CAR),
        (OTHER, OTHER),
    )

    car = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        choices=CHOICES,
        verbose_name='Type'
    )

    model = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(2),
        ),
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            valid_year_validator,
        )
    )

    car_image = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(1),
        )
    )

    def __str__(self):
        return f'{self.car} {self.model}'
