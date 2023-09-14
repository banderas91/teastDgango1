# main/urls.py

from django.urls import path
from main import views
urlpatterns = [
    path('', views.index),
]

# myshop/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
path('clients/<int:client_id>/', views.client_detail, name='client_detail'),
path('products/<int:product_id>/', views.product_detail, name='product_detail'), 
path('orders/<int:order_id>/', views.order_detail, name='order_detail')
