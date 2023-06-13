from django.db import models


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    FICTION = 'Fiction'
    NOVEL = 'Novel'
    CRIME = 'Crime'

    BOOK_TYPES = (
        (FICTION, FICTION),
        (NOVEL, NOVEL),
        (CRIME, CRIME),
    )

    title = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    image = models.URLField(
        null=False,
        blank=False,
    )

    type = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=BOOK_TYPES,
    )

    def __str__(self):
        return self.title
