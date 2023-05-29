from django.contrib import admin

from petstagram.accounts.models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_filter = ('id', 'username', 'email')
    search_fields = ('id', 'username', 'email')
