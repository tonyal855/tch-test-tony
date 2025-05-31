from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('accounts/login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('create_user/', views.create_user, name='create_user'),
]