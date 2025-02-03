from django.urls import path
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    path('', views.index, name="homepage"),
    path('products/<product_name>/<product_slug>', views.product_page, name="product_page"),
    path('categories/<category_name>/<category_slug>', views.category_page, name="category_page")
]















