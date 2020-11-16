from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date', 'stripe_pid')

    fields = ('service_name', 'order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'stripe_pid', 'total_amount',)

    list_display = ('order_number', 'date', )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
