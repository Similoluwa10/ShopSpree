import uuid
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from orders.models import Order
from .models import PaymentRecord
from .gateways.paystack import PaystackGateway


def _get_gateway():
    """Factory function — swap this to change payment provider."""
    return PaystackGateway()


@login_required
def initiate_payment(request, order_id):
    """Initiate payment for an order via the configured payment gateway."""
    order = get_object_or_404(Order, pk=order_id, user=request.user)

    if order.status not in ('pending', 'confirmed'):
        return JsonResponse({"error": "This order cannot be paid for."}, status=400)

    gateway = _get_gateway()
    reference = f"SHOPSPREE-{order.pk}-{uuid.uuid4().hex[:8]}"

    # Create a payment record before calling the gateway
    payment = PaymentRecord.objects.create(
        order=order,
        user=request.user,
        gateway='paystack',
        reference=reference,
        amount=order.total_amount,
        status='initiated',
    )

    try:
        result = gateway.initiate(
            email=request.user.email,
            amount=float(order.total_amount),
            reference=reference,
            callback_url=request.build_absolute_uri(
                reverse('payments:verify_payment', args=[payment.pk])
            ),
        )
        return redirect(result['authorization_url'])

    except Exception as e:
        payment.status = 'failed'
        payment.save()
        return JsonResponse({"error": str(e)}, status=500)


@login_required
def verify_payment(request, payment_id):
    """Verify payment status via the gateway and update order accordingly."""
    payment = get_object_or_404(PaymentRecord, pk=payment_id, user=request.user)
    gateway = _get_gateway()

    result = gateway.verify(payment.reference)
    payment.gateway_response = result['raw']

    if result['status'] == 'success':
        payment.status = 'success'
        payment.save()

        # Mark the order as paid
        order = payment.order
        order.status = 'paid'
        order.save()

        return redirect('orders:order_detail', order_id=order.pk)
    else:
        payment.status = 'failed'
        payment.save()
        return redirect('orders:order_detail', order_id=payment.order.pk)
