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

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-publication_date_time']
        verbose_name_plural = 'Comments'


class Like(models.Model):
    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )
