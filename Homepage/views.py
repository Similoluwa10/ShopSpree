from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, ProductGroup


def index(request):
    products = Product.objects.all()
    product_groups = ProductGroup.objects.all()
    return render(request, 'index.html', {'products': products, 'product_groups': product_groups})














