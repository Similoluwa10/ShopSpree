from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.models import Cart, CartItem


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
    related_products = Product.objects.filter(
        categories__in=product.categories.all()
    ).exclude(pk=product.pk).distinct()[:6]

    # Check if product is already in the user's cart
    cart_quantity = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            cart_item = CartItem.objects.filter(cart=cart, product=product).first()
            if cart_item:
                cart_quantity = cart_item.quantity

    return render(request, 'productpage.html', {
        'product': product,
        'related_products': related_products,
        'cart_quantity': cart_quantity,
    })


def category_page(request, category_name, category_slug):
    """View for category pages showing products in that category."""
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(categories=category)
    return render(request, 'categorypage.html', {
        'category': category,
        'products': products,
    })


def product_search(request):
    """Search products by name."""
    query = request.GET.get('q', '').strip()
    products = Product.objects.none()

    if query:
        products = Product.objects.filter(name__icontains=query)

    return render(request, 'search_results.html', {
        'products': products,
        'query': query,
    })
