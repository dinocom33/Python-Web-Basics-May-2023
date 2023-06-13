from django.contrib import admin

from library_app.core.models import Profile, Book


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'description')
    search_fields = ('title', 'type')
    list_filter = ('title', 'type')
