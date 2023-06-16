from django.urls import path

from .views import album_details, add_album, delete_album, edit_album


urlpatterns = [
    path('add/', add_album, name='add album'),
    path('delete/<int:pk>/', delete_album, name='delete album'),
    path('edit/<int:pk>/', edit_album, name='edit album'),
    path('details/<int:pk>/', album_details, name='album details'),
]
