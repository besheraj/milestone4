from django.shortcuts import render,redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ServiceForm
from .models import Service


@login_required
def services(request):
    # display all quizes
    services = Service.objects.all()
    context = {
        'services': services
    }
    return render(request, 'services/service.html', context)


@login_required
def quizz(request, service_id):
    # display a the quizz
    service = get_object_or_404(Service, pk=service_id)
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
            return redirect(reverse('quizz'))
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
            return redirect(reverse('quizz', args=[service.id]))
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