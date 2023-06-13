from django.core import validators
from django.db import models

from my_music_app.main.validators import validate_only_alphanumeric


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(2),
            validate_only_alphanumeric,
        )
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username


class Album(models.Model):
    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = "Jazz Music"
    RNB_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER_MUSIC = "Other"

    CHOICES = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_MUSIC, RNB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
        (OTHER_MUSIC, OTHER_MUSIC),
    )

    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=True,
    )
    artist = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    genre = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=CHOICES,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(0.0),
        )
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('pk',)
