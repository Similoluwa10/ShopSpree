from django.shortcuts import render
from catalog.models import Product, Category


def homepage(request):
    """Homepage view — assembles featured products and categories from the catalog."""
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'storefront/index.html', {
        'products': products,
        'categories': categories,
    })
