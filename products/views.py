
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Product, Category, User
from django.contrib import messages
from .forms import LoginForm, SignupForm



# View for homepage
def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {'products': products, 'categories': categories,})


#View for product pages
def product_page(request, product_name, product_slug):
    product = Product.objects.get(slug = product_slug)
    return render(request, 'productpage.html', {'product': product,})


#View for category pages
def category_page(request, category_name, category_slug):
    category = Category.objects.get(slug = category_slug)
    return render(request, 'categorypage.html', {'category': category,})


