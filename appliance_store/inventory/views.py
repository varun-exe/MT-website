from django.shortcuts import render
from .models import Product

def inventory_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/inventory_list.html', {'products': products})
