from django.core import validators
from django.db import models


class Album(models.Model):
    ALBUM_TYPES = (
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Country Music', 'Country Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip Hop Music', 'Hip Hop Music'),
        ('Other', 'Other'),
    )

    name = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False,
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
        choices=ALBUM_TYPES
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            validators.MinValueValidator(0.0),
        ]
    )
