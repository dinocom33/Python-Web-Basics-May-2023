from django.contrib import admin
from django.urls import path, include

import my_music_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_music_app.main.urls'))
]
