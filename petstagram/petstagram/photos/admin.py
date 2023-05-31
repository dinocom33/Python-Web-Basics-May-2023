from django.contrib import admin

from petstagram.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'publication_date', 'description', 'location', 'pets')
    list_filter = ('publication_date', 'tagged_pets', 'description')
    search_fields = ('publication_date', 'tagged_pets')

    @staticmethod
    def pets(obj):
        tagged_pets = obj.tagged_pets.all()
        if tagged_pets:
            return ', '.join(p.name for p in tagged_pets)
        return 'No tagged pets'
