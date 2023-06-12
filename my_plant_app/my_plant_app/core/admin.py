from django.contrib import admin

from my_plant_app.core.models import Profile, Plant


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('plant_name', 'plant_type', 'plant_description', 'price')
