from django.contrib import admin

from petstagram.pets.models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_of_birth', 'slug')
    list_filter = ('id', 'name', 'date_of_birth')
    search_fields = ('id', 'name', 'date_of_birth')
