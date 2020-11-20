from django.contrib import admin
from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('<int:service_id>', views.checkout, name='checkout'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('create_order/', views.create_order, name='create_order'),
    path('wh/', webhook, name='webhook')
]
