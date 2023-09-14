from django.db import models
from django import forms

class Client(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, default="Unnamed")
    last_name = models.CharField(max_length=100, default="Unnamed")
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name  

    def full_name(self):
        return f'{self.first_name} {self.last_name}'



class Product(models.Model):

  name = models.CharField(max_length=100)
  short_desc = models.CharField(max_length=100, default="Описание недоступно")
  full_desc = models.TextField(default="Описание отсутствует")
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  quantity = models.PositiveIntegerField()
  added_at = models.DateTimeField(auto_now_add=True)

  image = models.ImageField(upload_to='products_images/', default='default.jpg')
  
  def __str__(self):
    return self.name


class ProductForm(forms.ModelForm):

  class Meta:
    model = Product
    fields = ['name', 'description', 'price', 'image']


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2) 
    created_at = models.DateTimeField(auto_now_add=True)



from .models import Product