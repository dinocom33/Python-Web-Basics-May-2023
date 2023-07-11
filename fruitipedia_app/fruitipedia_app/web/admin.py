from django.contrib import admin

from fruitipedia_app.web.models import ProfileModel, FruitModel


@admin.register(ProfileModel)
class AdminProfileModel(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'age')
    list_filter = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


@admin.register(FruitModel)
class AdminFruitModel(admin.ModelAdmin):
    list_filter = ('name',)
    search_fields = ('name',)
