from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ServiceForm
from .models import Service

from checkout.models import Order
from profiles.models import UserProfile


@login_required
def services(request):
    # display all quizes
    services = Service.objects.all()
    profile = UserProfile.objects.get(user=request.user)
    orders = Order.objects.filter(user_profile=profile, status="paid")
    res = []

    for svc in services:
        current_svc = {
            "id": svc.id,
            "name": svc.name,
            "image": svc.image,
            "quizz": svc.quizz,
            "description": svc.description,
            "sku": svc.sku,
            "paid": False
        }
        for order in orders:
            if svc.id == order.service_id.id:
                current_svc["paid"] = True
                break
        res.append(current_svc)
    context = {
        'services': res
    }
    return render(request, 'services/service.html', context)


@login_required
def quizz(request, service_id):
    # show only quizz with successful payment
    profile = UserProfile.objects.get(user=request.user)
    orders = Order.objects.filter(service_id=service_id, user_profile=profile)
    if orders.count() == 0:
        messages.error(request, 'You have to buy the service first')
        return redirect(reverse('services'))
    else:
        order = orders.first()
        if order.status == 'paid':
            service = Service.objects.get(pk=service_id)
            context = {
                'service': service
            }
            return render(request, 'services/quizz.html', context)


@login_required()
def add_quizz(request):
    # add a quizz
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added !')
            return redirect(reverse('services'))
        else:
            messages.error(request, 'Failed to add service. Please ensure the form is valid.')
    else:
        form = ServiceForm()

    template = 'services/add_quizz.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_quizz(request, service_id):
    # edit a quizz
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    service = get_object_or_404(Service, pk=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated!')
            return redirect(reverse('services'))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ServiceForm(instance=service)
        messages.info(request, f'You are editing {service.name}')

    template = 'services/edit_quizz.html'
    context = {
        'form': form,
        'service': service,
    }

    return render(request, template, context)


@login_required
def delete_quizz(request, service_id):
    # delete a quizz
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    messages.success(request, 'Quizz deleted!')
    return redirect(reverse('services'))
