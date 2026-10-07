"""Paystack payment gateway implementation."""
import requests
from django.conf import settings
from .base import PaymentGateway


class PaystackGateway(PaymentGateway):
    """Paystack-specific implementation of the PaymentGateway interface."""

    def __init__(self):
        self.secret_key = settings.PAYSTACK_SECRET_KEY
        self.base_url = settings.PAYSTACK_BASE_URL

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.secret_key}",
            "Content-Type": "application/json",
        }

    def initiate(self, email, amount, reference, callback_url=None):
        """Initiate a Paystack transaction."""
        url = f"{self.base_url}/transaction/initialize"
        data = {
            "email": email,
            "amount": int(amount * 100),  # Convert to kobo
            "reference": reference,
        }
        if callback_url:
            data["callback_url"] = callback_url

        response = requests.post(url, json=data, headers=self._headers())
        response_data = response.json()

        if response.status_code == 200 and response_data.get("status") is True:
            return {
                "authorization_url": response_data["data"]["authorization_url"],
                "reference": response_data["data"]["reference"],
                "raw": response_data,
            }

        raise Exception(
            f"Paystack initialization failed: {response_data.get('message', 'Unknown error')}"
        )

    def verify(self, reference):
        """Verify a Paystack transaction by reference."""
        url = f"{self.base_url}/transaction/verify/{reference}"

        response = requests.get(url, headers=self._headers())
        response_data = response.json()

        if response.status_code == 200 and response_data.get("status") is True:
            data = response_data["data"]
            return {
                "status": data.get("status", "failed"),
                "amount": data.get("amount", 0) / 100,  # Convert from kobo
                "raw": response_data,
            }

        return {
            "status": "failed",
            "amount": 0,
            "raw": response_data,
        }
