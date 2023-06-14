from django.urls import path

from .views import profile_details, create_profile, details_note, add_note, edit_note, delete_note, index, \
    delete_profile

urlpatterns = [
    path('', index, name='index'),
    path('profile/', profile_details, name='profile details'),
    path('create_profile/', create_profile, name='create profile'),
    path('delete_profile/', delete_profile, name='delete profile'),
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('delete/<int:pk>/', delete_note, name='delete note'),
    path('details/<int:pk>/', details_note, name='details note'),
]
