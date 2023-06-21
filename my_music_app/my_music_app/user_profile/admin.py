from django.contrib import admin

from my_music_app.user_profile.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'age')
    list_filter = ('username', 'email', 'age')
    search_fields = ('username', 'email', 'age')