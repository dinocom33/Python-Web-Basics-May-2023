from django.contrib import admin

from car_collection.web.models import Profile, Car


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'age', 'first_name', 'last_name')
    search_fields = ['username', 'email', 'age', 'first_name', 'last_name']
    list_filter = ['username', 'email', 'age', 'first_name', 'last_name']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    fields = ['car', 'model', 'year', 'price']
    search_fields = ['car', 'model', 'year', 'price']
    list_filter = ['car', 'model', 'year', 'price']
