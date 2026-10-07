from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from .models import Order, OrderItem


@login_required
def checkout(request):
    """Checkout view — converts cart items into an order."""
    cart = Cart.objects.filter(user=request.user).first()

    if not cart or not cart.items.exists():
        return redirect('cart:cart_page')

    if request.method == 'POST':
        shipping_address = request.POST.get('shipping_address', '')

        # Create the order
        order = Order.objects.create(
            user=request.user,
            shipping_address=shipping_address,
            status='pending',
        )

        # Convert cart items to order items, snapshot current prices
        total = 0
        for cart_item in cart.items.select_related('product').all():
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price_at_purchase=cart_item.product.price,
            )
            total += cart_item.product.price * cart_item.quantity

        order.total_amount = total
        order.save()

        # Clear the cart after order is placed
        cart.items.all().delete()

        return redirect('orders:order_detail', order_id=order.pk)

    return render(request, 'orders/checkout.html', {'cart': cart})


@login_required
def order_detail(request, order_id):
    """View details of a specific order."""
    order = get_object_or_404(Order, pk=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})


@login_required
def order_history(request):
    """View all past orders for the authenticated user."""
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_history.html', {'orders': orders})
