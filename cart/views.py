from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
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

    # Support AJAX requests — return JSON instead of redirecting
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'quantity': cart_item.quantity,
            'item_total': str(cart_item.get_total_price()),
            'cart_total': str(cart.get_total_price()),
            'cart_item_count': cart.items.count(),
        })

    return redirect('cart:cart_page')


@login_required
def remove_from_cart(request, product_slug):
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Product, slug=product_slug)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    cart_item.delete()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'cart_total': str(cart.get_total_price()),
            'cart_item_count': cart.items.count(),
        })

    return redirect('cart:cart_page')


@login_required
@require_POST
def update_cart(request, product_slug):
    """Update the quantity of a cart item (increment or decrement via AJAX)."""
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Product, slug=product_slug)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)

    action = request.POST.get('action', 'increment')

    if action == 'increment':
        cart_item.quantity += 1
        cart_item.save()
    elif action == 'decrement':
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
            return JsonResponse({
                'success': True,
                'removed': True,
                'cart_total': str(cart.get_total_price()),
                'cart_item_count': cart.items.count(),
            })

    return JsonResponse({
        'success': True,
        'removed': False,
        'quantity': cart_item.quantity,
        'item_total': str(cart_item.get_total_price()),
        'cart_total': str(cart.get_total_price()),
        'cart_item_count': cart.items.count(),
    })


@login_required
def cart_detail(request):
    """Displays the cart page."""
    cart = Cart.objects.filter(user=request.user).first()
    return render(request, 'cart/cart.html', {'cart': cart})
