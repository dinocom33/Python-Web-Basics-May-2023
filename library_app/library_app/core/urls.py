from django.urls import path, include

from library_app.core.views import index, profile_details, delete_profile, edit_profile, book_details, edit_book, \
    add_book, create_profile, delete_book

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_book, name='add_book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('details/<int:pk>/', book_details, name='book details'),
    path('delete/', delete_book, name='delete book'),
    path('profile/', include([
        path('', profile_details, name='profile details'),
        path('create/', create_profile, name='create profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ]))
]
