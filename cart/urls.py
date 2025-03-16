from django.urls import path, include
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<slug:product_slug>/', views.add_to_cart, name='cart_add'),
    path('remove/<slug:product_slug>/', views.remove_from_cart, name='cart_remove'),
    path('', views.cart_detail, name='cart_page'),
       
]


