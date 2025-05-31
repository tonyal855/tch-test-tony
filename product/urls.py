from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_module, name='module'),
    path('module/', views.list_module, name='module'),
    path('install/', views.create_module, name='create_module'),
    path('upgrade/', views.upgrade, name='upgrade'),
    path('create_field/', views.create_field, name='create_field'),
    path('remove_field/<int:id>', views.remove_field, name='remove_field'),
    path('uninstall/', views.remove_module, name='remove_module'),
    path('product/', views.product, name='product'),
    path('create_product/', views.create_product, name='create_product'),
    path('update_product/<int:id>', views.update_product, name='update_product'),
    path('remove_product/<int:id>', views.remove_product, name='remove_product'),
]