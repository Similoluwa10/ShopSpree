from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('search/', views.product_search, name='product_search'),
    path('<product_name>/<product_slug>/', views.product_page, name='product_page'),
    path('category/<category_name>/<category_slug>/', views.category_page, name='category_page'),
]
