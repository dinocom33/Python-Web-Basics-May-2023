from django.urls import path, include

from fruitipedia_app.web.views import index, dashboard, create_fruit, fruit_details, edit_fruit, delete_fruit, create_profile, \
    delete_profile, details_profile, edit_profile

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create/', create_fruit, name='create fruit'),
    path('<int:pk>/', include([
        path('details/', fruit_details, name='fruit details'),
        path('edit/', edit_fruit, name='edit fruit'),
        path('delete/', delete_fruit, name='delete fruit'),
    ])),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ]))
]
