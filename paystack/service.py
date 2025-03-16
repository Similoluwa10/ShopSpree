
import requests
from django.conf import settings
from cart.models import Cart

PAYSTACK_SECRET_KEY = settings.PAYSTACK_SECRET_KEY
PAYSTACK_BASE_URL = "https://api.paystack.co"


# Function to initiate paystack payment
def initiate_payment(request):
    email = request.user.email
    this_cart = Cart.objects.get(user=request.user)
    amount = this_cart.get_total_price()
    
    url = f"{PAYSTACK_BASE_URL}/transaction/initialize"
    
    headers = {
        "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json"
    }   
    data = {
        "email": email,
        "amount": int(amount * 100)  # Convert to kobo
    }
    response = requests.post(url, json=data, headers=headers)
        
    if response.status_code == 200:
        pass
        return response.json()
    return None

    


def verify_payment(reference):
    """
    Verify a payment using Paystack.
    :param reference: Payment reference
    :return: Response data or None
    """
    url = f"{PAYSTACK_BASE_URL}/transaction/verify/{reference}"
    headers = {
        "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None
