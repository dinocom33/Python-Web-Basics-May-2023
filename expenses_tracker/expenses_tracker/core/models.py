from django.core import validators
from django.db import models

from .validators import validate_only_alpha, file_size_validator


class Profile(models.Model):
    first_name = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(2),
            validate_only_alpha,
        )
    )

    last_name = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(2),
            validate_only_alpha,
        )
    )

    budget = models.FloatField(
        null=False,
        blank=False,
        default=0,
        validators=(
            validators.MinValueValidator(0),
        )
    )

    profile_image = models.ImageField(
        upload_to='profile_images/',
        null=True,
        blank=True,
        validators=(
            file_size_validator,
        )
    )

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Expense(models.Model):
    titles = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name='Title'
    )

    expense_image = models.URLField(
        null=False,
        blank=False,
        verbose_name='Link to Image',
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.titles

    class Meta:
        ordering = ('titles', 'price')
