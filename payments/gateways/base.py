"""
Abstract base class for payment gateways.
All gateway implementations must subclass this.
"""
from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    """Interface that all payment gateway backends must implement."""

    @abstractmethod
    def initiate(self, email, amount, reference, callback_url=None):
        """
        Start a payment transaction.

        Args:
            email: Customer email address.
            amount: Amount in the currency's major unit (e.g. Naira, not kobo).
            reference: A unique reference string for this transaction.
            callback_url: Optional URL the gateway should redirect to after payment.

        Returns:
            dict with at least:
                - 'authorization_url': URL to redirect the customer to.
                - 'reference': The transaction reference.
        """
        pass

    @abstractmethod
    def verify(self, reference):
        """
        Verify the status of a transaction.

        Args:
            reference: The transaction reference to verify.

        Returns:
            dict with at least:
                - 'status': 'success' | 'failed' | 'abandoned'
                - 'amount': Verified amount.
                - 'raw': The full gateway response dict.
        """
        pass
