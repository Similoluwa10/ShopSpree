from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from catalog.models import Product
from .models import Cart, CartItem


@login_required
def add_to_cart(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    # Get or create cart for user
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if item already exists in cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart:cart_page')


@login_required
def remove_from_cart(request, product_slug):
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Product, slug=product_slug)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    cart_item.delete()
    return redirect('cart:cart_page')


@login_required
def cart_detail(request):
    """Displays the cart page."""
    cart = Cart.objects.filter(user=request.user).first()
    return render(request, 'cart/cart.html', {'cart': cart})
