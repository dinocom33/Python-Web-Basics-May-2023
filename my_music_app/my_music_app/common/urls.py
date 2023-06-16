from django.urls import path

from my_music_app.common.views import index

urlpatterns = [
    path('', index, name='index'),
]
