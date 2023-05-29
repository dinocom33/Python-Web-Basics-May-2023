from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from .validators import file_size_validator


class Photo(models.Model):
    MAX_DESCRIPTION_LENGTH = 300
    MIN_DESCRIPTION_LENGTH = 10

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='media/pet_photos/',
        null=False,
        blank=True,
        validators=(file_size_validator,),
    )
    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(MinLengthValidator(MIN_DESCRIPTION_LENGTH),),
        null=True,
        blank=True,
    )
    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
    )
    publication_date = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )
    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )
