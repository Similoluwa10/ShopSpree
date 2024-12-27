
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


def login_page(request):
    if request.method == 'POST':     
        login_form = LoginForm(request.POST)  
        is_loggedin = False
        if login_form.is_valid():
            users = User.objects.all()   
                  
            for user in users:                
                if user.email == login_form.cleaned_data['email'] and user.password == login_form.cleaned_data['password']:
                    user.is_authenticated = True
                    is_loggedin = True
                    username = user.username
                else:
                    username = 'account does not exist'
                       
    login_form = LoginForm()                               
    return render(request, 'login.html', {'login_form': login_form,}) 


def signup_page(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            signup_account = User(
                username = signup_form.cleaned_data['username'],
                email = signup_form.cleaned_data['email'],
                password = signup_form.cleaned_data['password']
            ) 
            signup_account.save()           
            signup_form = SignupForm() 
    
    signup_form = SignupForm()                             
    return render(request, 'signup.html', {'signup_form': signup_form,}) 



#View for product pages
def product_page(request, product_name, product_slug):
    product = Product.objects.get(slug = product_slug)
    return render(request, 'productpage.html', {'product': product,})


#View for category pages
def category_page(request, category_name, category_slug):
    category = Category.objects.get(slug = category_slug)
    return render(request, 'categorypage.html', {'category': category,})
