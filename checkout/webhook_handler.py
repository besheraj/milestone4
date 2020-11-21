from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order
from profiles.models import UserProfile

import time


class StripeWH_Handler:

    #  stripe webhook handler
    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        # once order success send confirmation email
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        # Handle a generic/unknown/unexpected webhook event
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):

        # if the payment succeeded webhook from Stripe
        intent = event.data.object
        order_id = intent.metadata.order_id

        order_exists = False
        order=None
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    order_number=order_id
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            order.status = "paid"
            order.save()
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | Order Doesn\'t exist',
                status=500)

    def handle_payment_intent_payment_failed(self, event):

        # if payment not successful
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
