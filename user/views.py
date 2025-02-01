
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, SignupForm
from django.contrib.auth.models import User


def login_user(request):
    if request.method == 'POST':
  
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            # messages.success(request, f' welcome {username} !!')
            return redirect('/')
        else:
            # messages.info(request, f'account done not exit plz sign in')
            pass
        
    login_form = LoginForm()
    return render(request, 'login.html', {'login_form':login_form})
     

def logout_user(request):
    logout(request)
    return redirect('/')


def signup_user(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            username = signup_form.cleaned_data['username']
            email = signup_form.cleaned_data['email']
            password = signup_form.cleaned_data['password']
            
            signup_account = User(
                username = username,
                email = email,
            ) 
            
            signup_account.set_password(password)
            print(username, email, password, signup_account)
            signup_account.save()           
            signup_form = SignupForm() 
    
    signup_form = SignupForm()                             
    return render(request, 'signup.html', {'signup_form': signup_form,}) 


