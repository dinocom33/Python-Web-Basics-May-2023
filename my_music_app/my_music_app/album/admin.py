from django.contrib import admin

from my_music_app.album.models import Album


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'genre', 'price')
    list_filter = ('artist', 'genre', 'price')
    search_fields = ('name', 'artist', 'genre', 'price')
