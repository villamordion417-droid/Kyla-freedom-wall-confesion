from django.urls import path
from . import views

urlpatterns = [
    # Change 'landing_page' to 'landing_view'
    path('', views.landing_view, name='landing'), 
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_view, name='upload'),
    path('wall/', views.wall_view, name='wall'),
    path('candle/<int:post_id>/', views.light_candle, name='light_candle'),
]