from django.core import validators
from django.db import models


class Profile(models.Model):
    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
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
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    image = models.URLField(
        null=True,
        blank=True,
    )

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.get_full_name()


class Game(models.Model):
    ACTION = 'Action'
    ADVENTURE = 'Adventure'
    PUZZLE = 'Puzzle'
    STRATEGY = 'Strategy'
    SPORTS = 'Sports'
    BOARD_CARD_GAME = 'Board/Card Game'
    OTHER = 'Other'

    GAME_CHOICES = (
        ('ACTION', ACTION),
        ('ADVENTURE', ADVENTURE),
        ('PUZZLE', PUZZLE),
        ('STRATEGY', STRATEGY),
        ('SPORTS', SPORTS),
        ('BOARD_CARD_GAME', BOARD_CARD_GAME),
        ('OTHER', OTHER),
    )

    title = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=15,
        null=False,
        blank=False,
        choices=GAME_CHOICES,
    )

    rating = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(0.1),
            validators.MaxValueValidator(5.0),
        )
    )

    max_level = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(1),
        )
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    summary = models.TextField(
        null=False,
        blank=False,
    )
