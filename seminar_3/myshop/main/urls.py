# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), 
    path('clients/<int:client_id>/orders/', views.client_orders, name='client_orders'),
]