# main/urls.py

from django.urls import path
from . import views
from main.views import client_detail, product_detail, order_detail
from main.views import order_detail
urlpatterns = [
    path('', views.index), 
    path('clients/<int:client_id>/orders/', views.client_orders, name='client_orders'),
    path('add-product/', views.add_product, name='add_product'),
    path('clients/<int:client_id>/', client_detail, name='client_detail'), 

    path('products/<int:product_id>/', product_detail, name='product_detail'),

    path('orders/<int:order_id>/', order_detail, name='order_detail'),
    
]


