from django.contrib import admin
from django.contrib.admin import models, ModelAdmin

from my_music_app.main.models import Profile, Album


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    pass


@admin.register(Album)
class AlbumAdmin(ModelAdmin):
    pass
