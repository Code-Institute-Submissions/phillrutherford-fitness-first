from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import SubscriptionForm

# Create your views here.
def subscription(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "No Subscription selected yet.")
        return redirect(reverse, ('workouts'))

    subscription_form = SubscriptionForm()
    template = /subscriptions/subscription.html
    context = {
        'subscription_form' = subscription_form
    }

    return render(request, template, context)
