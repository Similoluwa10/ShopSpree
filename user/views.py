
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
            messages.success(request, "Your account has been created successfully!")
            return redirect("login_page")          
    
    signup_form = SignupForm()                             
    return render(request, 'signup.html', {'signup_form': signup_form,}) 




# signup_form = SignupForm(request.POST)

# serializer = DrinkSerializer(data=request.data)

# These are both ways of getting data from a form, 
# but can you explain both of them and how they work differently, 
# and also, can you explain how exactly data is gotten from a form or a post request

