from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=30)
    # first_name = models.CharField(max_length=30, null=True, blank=True)
    # last_name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('username',)