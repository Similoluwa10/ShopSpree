from django.contrib import admin
from .models import Product, ProductGroup, Cart, User


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class ProductGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGroup, ProductGroupAdmin)
admin.site.register(Cart)
admin.site.register(User)