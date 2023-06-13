from django.contrib import admin
from django.contrib.admin import models, ModelAdmin

from my_music_app.main.models import Profile, Album


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'age')
    search_fields = ('username', 'email', 'age')
    list_filter = ('username', 'email', 'age')


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'artist', 'genre', 'description', 'price']
    search_fields = ('name', 'artist', 'genre', 'price')
    list_filter = ('name', 'artist', 'genre', 'price')
