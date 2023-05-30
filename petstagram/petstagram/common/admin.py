from django.contrib import admin

from petstagram.common.models import Comments


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    pass
