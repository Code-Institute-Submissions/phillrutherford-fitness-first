from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import SubscriptionForm

import stripe

# Create your views here.
def subscription(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    subscription_total = 6.99
    total = 6.99

    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    print(intent)

    intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    Subscription_form = SubscriptionForm()
    template = 'subscriptions/subscriptions.html'
    context = {
        'Subscription_form': Subscription_form,
        'stripe_public_key': 'pk_test_51IPe6YEDQ5VY803KilcwszsHwmiokZWV3YaCoWRM8EAb0hFAIXzefeC5i0gIfZjxE32vl2PJJxYAOQKHgoqujqNt00PA3jtd3l',
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

def subscription_success(request, subscription_number):
    """
    Handle successful subscriptions
    """
    save_info = request.session.get('save_info')
    subscription = get_object_or_404(Subscription, subscription_number=subscription_number)
    messages.success(request, f'Subscription successfully processed! \
        Your order number is {subscription_number}. A confirmation \
        email will be sent to {subscription.email}.')

    if 'TODO' in request.session:
        del request.session['TODO']

    template = 'subscription/subscription_success.html'
    context = {
        'subscription': subscription,
    }

    return render(request, template, context)
