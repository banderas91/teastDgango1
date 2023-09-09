from django.shortcuts import render
# from httpx import Client

from .models import Order 
from datetime import datetime, timedelta




def client_orders(request, client_id):

    client = Client.objects.get(id=client_id)
    
    orders = Order.objects.filter(client=client)

    context = {'orders': orders}
    
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

