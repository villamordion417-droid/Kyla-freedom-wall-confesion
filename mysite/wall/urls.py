from django.urls import path

from . import views

app_name = 'wall'

urlpatterns = [
    path('', views.landing_view, name='landing'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_view, name='upload'),
    path('wall/', views.wall_view, name='wall'),
    path('api/light_candle/<int:post_id>/', views.light_candle, name='light_candle'),
]