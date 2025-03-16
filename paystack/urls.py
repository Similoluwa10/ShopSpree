from django.urls import path
from . import service

app_name = 'pay'

urlpatterns = [
    path('initiate_payment', service.initiate_payment, name='initiate_payment'),
    path('verify_payment', service.verify_payment, name='verify_payment')
]