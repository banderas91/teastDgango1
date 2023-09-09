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

