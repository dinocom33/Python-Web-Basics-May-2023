from django.contrib import admin

from games_play_app.core.models import Profile, Game


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'email')
    search_fields = ('first_name', 'last_name', 'age', 'email')
    list_filter = ('first_name', 'last_name', 'age', 'email')


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'rating', 'max_level', 'summary')
    search_fields = ('title', 'category', 'rating', 'max_level')
    list_filter = ('title', 'category', 'rating', 'max_level')
