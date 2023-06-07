from django.urls import path, include

from car_collection.web.views import index, profile_details, delete_profile, edit_profile, create_profile, \
    car_details, catalogue, create_car, edit_car, delete_car

urlpatterns = [
    path('', index, name='index'),
    path('catalogue', catalogue, name='catalogue'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', profile_details, name='profile details'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
        path('car/', include(([
            path('create/', create_car, name='create car'),
            path('<int:pk>/details/', car_details, name='car details'),
            path('<int:pk>/edit/', edit_car, name='edit car'),
            path('<int:pk>/delete/', delete_car, name='delete car'),
        ]))),
    ]))
]
