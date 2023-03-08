from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('create/', views.user_create, name='create'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),    
]