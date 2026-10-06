# Used to alert a login required message

from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # If user is not authenticated and trying to access a protected page
        if not request.user.is_authenticated and request.path.startswith('/cart/'):
            messages.warning(request, "You need to log in to add items to your cart.")
            return redirect(f"{reverse('login_page')}?next={request.path}")

        return self.get_response(request)





