from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django_password_eye.fields import PasswordEye

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    # username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)  
    email = forms.EmailField()
    phone_number = PhoneNumberField(label='Phone Number', widget=forms.TextInput(attrs={'placeholder': 'e.g., +234 123 456 7890'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    password = PasswordEye(label='password')
    confirm_password = PasswordEye(label='confirm password')
    

class OtpForm(forms.Form):
    otp = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'placeholder': 'Enter your OTP'}))   