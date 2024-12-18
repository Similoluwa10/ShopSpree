from django.urls import path
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    path('', views.index, name="homepage"),
    path('login_page', views.login_page, name="login_page"),
    # path('login_page', LoginView.as_view(template_name='login.html'), name='login_page'),
]















