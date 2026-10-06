
import requests
from django.http import JsonResponse, HttpResponseRedirect
from django.conf import settings
from cart.models import Cart

def initiate_payment(request):
    PAYSTACK_SECRET_KEY = settings.PAYSTACK_SECRET_KEY
    email = request.user.email
    this_cart = Cart.objects.get(user=request.user)
    amount = this_cart.get_total_price()
    url = f"{settings.PAYSTACK_BASE_URL}/transaction/initialize"

    headers = {
        "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "email": email,
        "amount": int(amount * 100)  # Convert to kobo
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response_data = response.json()
        
        if response.status_code == 200 and response_data.get("status") is True:
            authorization_url = response_data["data"]["authorization_url"]
            
            return HttpResponseRedirect(authorization_url)  # Redirect user to Paystack checkout
        
        return JsonResponse({"error": "Payment initialization failed"}, status=response.status_code)
    
    except requests.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)

