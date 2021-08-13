from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        # to stop people manually accessing checkout with url manipulation
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JO31YC1T33UiaHX5sysHpmzL6aDYZ8ebuPoMSRTm2WbfF8e2qQE9yTa47Ze3ewMfj0WvOQOtUk3YVph4EMHhyOQ00YPDwV3I0',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
