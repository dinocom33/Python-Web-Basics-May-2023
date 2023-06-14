from django.db import models


class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Note(models.Model):
    title = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    content = models.TextField(
        null=False,
        blank=False,
    )
