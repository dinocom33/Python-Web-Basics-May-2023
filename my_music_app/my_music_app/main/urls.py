from django.urls import path, include

from .views import index, add_album, album_details, delete_album, edit_album, profile_details, delete_profile, \
    add_profile

urlpatterns = [
    path('', index, name='index'),
    path('album/', include([
        path('add', add_album, name='add album'),
        path('details/<int:pk>/', album_details, name='details album'),
        path('edit/<int:pk>/', edit_album, name='edit album'),
        path('delete/<int:pk>/', delete_album, name='delete album'),
    ])),
    path('profile/', include([
        path('add/', add_profile, name='add profile'),
        path('details', profile_details, name='profile details'),
        path('delete', delete_profile, name='delete profile'),
    ])),
]
