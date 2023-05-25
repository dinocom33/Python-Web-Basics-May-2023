from django.contrib import admin

from petstagram.accounts.models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    pass
