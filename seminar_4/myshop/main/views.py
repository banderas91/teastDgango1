import logging
from django.shortcuts import render
from flask import redirect
from main.models import Client, Order  
# from datetime import datetime, timedelta
# logger = logging.getLogger('orders_filter')


# today = datetime.now().date()
# week_ago = today - timedelta(days=7)

# week_orders = Order.objects.filter(created_at__gte=week_ago).query
# logger.info('Weeks orders query: %s', week_orders)

# month_ago = today - timedelta(days=30)
# month_orders = Order.objects.filter(created_at__gte=month_ago).query 
# logger.info('Month orders query: %s', month_orders)

# year_ago = today - timedelta(days=365)
# year_orders = Order.objects.filter(created_at__gte=year_ago).query
# logger.info('Year orders query: %s', year_orders)




from datetime import datetime, timedelta
from .models import Order
from .forms import ProductForm

def client_orders(request, client_id):

  client = Client.objects.get(id=client_id)
  
  orders = Order.objects.filter(client=client)

  today = datetime.now().date()  

  week_ago = today - timedelta(days=7)
  month_ago = today - timedelta(days=30)
  year_ago = today - timedelta(days=365)

  week_orders = orders.filter(created_at__gte=week_ago)
  month_orders = orders.filter(created_at__gte=month_ago)
  year_orders = orders.filter(created_at__gte=year_ago)

  context = {
    'orders': orders,
    'week_orders': week_orders,
    'month_orders': month_orders,
    'year_orders': year_orders
  }

  return render(request, 'main/client_orders.html', context)

def index(request):
    return render(request, 'main/index.html')


def client_orders(request, client_id):

  client = Client.objects.get(id=client_id)
  
  orders = Order.objects.filter(client=client)

  today = datetime.now().date()

  week_ago = today - timedelta(days=7)
  month_ago = today - timedelta(days=30)
  year_ago = today - timedelta(days=365)  

  week_orders = orders.filter(created_at__gte=week_ago)
  month_orders = orders.filter(created_at__gte=month_ago)
  year_orders = orders.filter(created_at__gte=year_ago)

  context = {
    'orders': orders,
    'week_orders': week_orders,
    'month_orders': month_orders,
    'year_orders': year_orders
  }


  return render(request, 'main/client_orders.html', context)

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():  
            product = form.save()
            return redirect('product_detail', product.id)

    form = ProductForm()
    return render(request, 'add_product.html', {'form': form})