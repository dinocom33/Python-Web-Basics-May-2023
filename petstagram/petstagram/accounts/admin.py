from django.contrib import admin
from django.contrib.auth.models import User


class MyUserAdmin(admin.ModelAdmin):
    # fields = [('username', 'password'), ('first_name', 'last_name'), 'email']
    search_fields = ['first_name', 'last_name', 'username', 'email']
    list_filter = ['username', 'first_name', 'last_name']
    fieldsets = (
        ('Login info',
         {'fields': ('username', 'password')}),
        ('Personal info',
         {'fields': ('first_name', 'last_name', 'email')}),
    )


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
