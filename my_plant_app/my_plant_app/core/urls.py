from django.urls import path, include

from .views import create_profile, catalogue, create_plant, profile_details, plant_details, edit_profile, edit_plant, \
    delete_plant, delete_profile, index

urlpatterns = [
    path('', index, name='index'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', profile_details, name='profile details'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
    path('catalogue', catalogue, name='catalogue'),
    path('create/', create_plant, name='create plant'),
    path('details/<int:pk>/', plant_details, name='plant details'),
    path('edit/<int:pk>/', edit_plant, name='edit plant'),
    path('delete/<int:pk>/', delete_plant, name='delete plant'),
]
