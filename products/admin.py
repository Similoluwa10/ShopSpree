from django.contrib import admin
from .models import Product, Category, Cart, User


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Cart)
admin.site.register(User)