
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
from django.contrib import messages
from .forms import LoginForm, SignupForm
from .models import User

# def login_user(request):
#     if request.method == 'POST':     
#         login_form = LoginForm(request.POST)  
#         if login_form.is_valid():
#             users = User.objects.all()         
#             for user in users:                
#                 if user.email == login_form.cleaned_data['email'] and user.password == login_form.cleaned_data['password']:
#                     login(request, user)
#                     return redirect('index')
#                 else:
#                     username = 'account does not exist'
                       
#     login_form = LoginForm()                               
#     return render(request, 'login.html', {'login_form': login_form,}) 

def login_user(request):
    if request.method == 'POST':     
        login_form = LoginForm(request.POST)  
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']

            # Use Django's authenticate to validate credentials
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('')
            else:
                return render(request, 'login.html', {
                    'login_form': login_form,
                    'error': 'Invalid email or password.'
                })
    
    login_form = LoginForm()                               
    return render(request, 'login.html', {'login_form': login_form})

        

def logout_user(request):
    logout(request)
    return redirect('index')


def signup_user(request):
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


