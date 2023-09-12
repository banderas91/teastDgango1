# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), 
    path('clients/<int:client_id>/orders/', views.client_orders, name='client_orders'),
    path('add-product/', views.add_product, name='add_product')
]

