from django.db import models

from petstagram.photos.models import Photo


class Comments(models.Model):
    text = models.CharField(
        max_length=300,
        null=False,
        blank=False,
    )
    publication_date_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )


class Like(models.Model):
    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )
