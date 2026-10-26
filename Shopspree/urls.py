"""
URL configuration for Shopspree project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# from two_factor.urls import urlpatterns as two_factor_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('storefront.urls')),
    path('products/', include('catalog.urls')),
    path('user/', include('user.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('payments/', include('payments.urls')),
    # path('', include(two_factor_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
