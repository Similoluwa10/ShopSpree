from django.contrib import admin
from .models import Product, ProductGroup

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

admin.site.register(Product, ProductAdmin)

class ProductGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_url')

admin.site.register(ProductGroup, ProductGroupAdmin)