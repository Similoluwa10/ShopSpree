from django.urls import path
from .views import homepage

app_name = 'storefront'

urlpatterns = [
    path('', homepage, name='homepage'),
]
