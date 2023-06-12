from django.urls import path, include

from games_play_app.core.views import index, profile_details, delete_profile, create_profile, edit_profile, \
    dashboard, game_details, edit_game, create_game, delete_game

urlpatterns = [
    path('', index, name='index'),
    path('dashboard', dashboard, name='dashboard'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', profile_details, name='profile details'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
    path('game/', include([
        path('create/', create_game, name='create game'),
        path('details/<int:pk>/', game_details, name='game details'),
        path('edit/<int:pk>/', edit_game, name='edit game'),
        path('delete/<int:pk>/', delete_game, name='delete game'),
    ])),
]
