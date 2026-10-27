
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from django.contrib import messages
from .forms import LoginForm, SignupForm, OtpForm
from django.contrib.auth.models import User
# from django_otp.decorators import otp_required
# from django_otp import send_otp
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username = email, password = password)
                
        if user is not None:
            login(request, user)
            # messages.success(request, f' welcome {username} !!')
            return redirect('/')
        else:
            messages.info(request, f'Incorrect Email or Password')
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
            # username = signup_form.cleaned_data['username']
            first_name = signup_form.cleaned_data['first_name']
            last_name = signup_form.cleaned_data['last_name']
            email = signup_form.cleaned_data['email']
            password = signup_form.cleaned_data['password'] 
            confirm_password = signup_form.cleaned_data['confirm_password']           

            if password != confirm_password:
                messages.info(request, 'Passwords do not match')
                return redirect('signup_page')

            try: 
                validate_password(password, user=None, password_validators=None)
            except ValidationError as e:
                for each in e:
                    messages.info(request, each)
                return redirect('signup_page')
            
            try:
                signup_account = User(
                    username = email,
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                ) 
                signup_account.set_password(password)
                signup_account.is_active = True
                signup_account.save() 
            except IntegrityError as e:
                messages.info(request, "Email already exists")
                return redirect('signup_page')            
            
            messages.success(request, "Your account has been created successfully!")
            return redirect("login_page") 
                     
    
    signup_form = SignupForm()                             
    return render(request, 'signup.html', {'signup_form': signup_form,}) 


def otp_verify(request):
    if request.method == 'POST':
        otp_form = OtpForm(request.POST)
        if otp_form.is_valid():
            otp = otp_form.cleaned_data['otp']
            
    otp_form = OtpForm()
    return render(request, 'otp.html', {'otp_form': otp_form})


def resend_otp(request):
    pass