from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

from .models import Service 

# Create your views here.
def all_services(request):
    services = Service.object.all()
    context = {
        'services':services
    }
    return render(request, 'services/service.html', context)

def products_details(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    context = {
        'services':service
    }
    return render(request, 'services/service_details.html', context)
