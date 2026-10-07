from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def product_list(request):
    """View for listing all products, with optional category filtering."""
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'catalog/product_list.html', {
        'products': products,
        'categories': categories,
    })


def product_page(request, product_name, product_slug):
    """View for individual product detail pages."""
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'catalog/product_detail.html', {'product': product})


def category_page(request, category_name, category_slug):
    """View for category pages showing products in that category."""
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'catalog/category_detail.html', {
        'category': category,
        'products': products,
    })
