from .models import Cart


def cart_count(request):
    """Makes cart_item_count available in all templates for the navbar badge."""
    count = 0
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        if cart:
            count = cart.items.count()
    return {'cart_item_count': count}
