from django.urls import path
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    path('login_page/', views.login_user, name="login_page"),
    path('logout/', views.logout_user, name="logout"),
    path('signup_page/', views.signup_user, name="signup_page"),
]


