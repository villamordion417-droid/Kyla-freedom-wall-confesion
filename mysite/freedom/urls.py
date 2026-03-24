from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wall.urls')), # This tells Django to look at your app for the homepage
]