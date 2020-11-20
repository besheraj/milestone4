from django.http import request
from services.views import services
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

from services.models import Service

from .forms import OrderForm
from .models import Order

from profiles.models import UserProfile
from profiles.forms import UserProfileForm

import stripe
from django.http import JsonResponse


@login_required
@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'username': request.user,
            'order_id': request.POST.get('order_id')
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


@login_required
@require_POST
def create_order(request):
    if request.method == 'POST':

        service_id = request.POST['service_id']
        profile = UserProfile.objects.get(user=request.user)
        orders = Order.objects.filter(
            service_id=service_id, user_profile=profile)
        if orders.count() > 0:
            return JsonResponse({'msg': 'you have already ordered this service, check your order history or available quizes.'},  status=400)

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            service_id = Service.objects.get(id=service_id)
            order.service_id = service_id
            profile = UserProfile.objects.get(user=request.user)
            # Attach the user's profile to the order
            order.user_profile = profile
            order.total_amount = settings.PRICE
            order.save()
            save_info = request.POST['save-info']
            
            if save_info:
                
                profile_data = {
                    'main_full_name': order.full_name,
                    'main_phone_number': order.phone_number,
                    'main_country': order.country,
                    'main_postcode': order.postcode,
                    'main_town_or_city': order.town_or_city,
                    'main_street_address1': order.street_address1,
                    'main_street_address2': order.street_address2,
                    'main_county': order.county,
                }
                
                user_profile_form = UserProfileForm(profile_data, instance=profile)
                if user_profile_form.is_valid():
                    user_profile_form.save()

            return JsonResponse({'order_id': order.order_number},  status=200)
        else:
            return JsonResponse({'msg': 'There was an error with your form. \
                Please double check your information.'},  status=400)


@login_required
def checkout(request, service_id):
    #  for check out and stripe
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    service = get_object_or_404(Service, pk=service_id)
        
    total = settings.PRICE
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    # prefill the user profile info if already stored before in profile
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'full_name': profile.main_full_name,
                'email': profile.user.email,
                'phone_number': profile.main_phone_number,
                'country': profile.main_country,
                'postcode': profile.main_postcode,
                'town_or_city': profile.main_town_or_city,
                'street_address1': profile.main_street_address1,
                'street_address2': profile.main_street_address2,
                'county': profile.main_county,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
    template = 'checkout/checkout.html'
    total = settings.PRICE
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'service': service,
        'total': settings.PRICE
    }
    return render(request, template, context)
