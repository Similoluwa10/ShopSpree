from django.urls import path
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    path('', views.index, name="homepage"),
    path('login_page', views.login_page, name="login_page"),
    path('signup_page', views.signup_page, name="signup_page"),
    path('products/<product_name>/<product_slug>', views.product_page, name="product_page"),
    path('categories/<category_name>/<category_slug>', views.category_page, name="category_page")
]















