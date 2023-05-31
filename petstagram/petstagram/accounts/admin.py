from django.contrib import admin
from django.contrib.auth.models import User


class MyUserAdmin(admin.ModelAdmin):
    fields = [('first_name', 'last_name'), ('username', 'password'), 'email']


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
