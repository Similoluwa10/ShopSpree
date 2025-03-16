
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Cart, CartItem
from paystack.service import initiate_payment



@login_required
def add_to_cart(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    # Print object for debugging
    print(product)
    
    # Get or create cart for user
    cart, created = Cart.objects.get_or_create(user=request.user)
    print(cart, created)
    # Check if item already exists in cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    print(cart_item, created)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart:cart_page')


@login_required
def remove_from_cart(request, product_slug):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product_slug)
    cart_item.delete()
    return redirect('cart:cart_page')

# displays the cart page
@login_required
def cart_detail(request):
    cart = Cart.objects.filter(user=request.user).first()
    return render(request, 'cart/cart.html', {'cart': cart})


# def checkout(request):
#     user_email = request.user.email
#     total_amount = add_to_cart(request)  
#     payment_response = initiate_payment(user_email, total_amount)
    
#     if payment_response and payment_response.get("status"):
#         return redirect(payment_response["data"]["url"])  # Redirect to Paystack payment page
    
#     # Handle payment initiation failure
#     return redirect("cart:checkout_failed")




