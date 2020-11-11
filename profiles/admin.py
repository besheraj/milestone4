from django.contrib import admin
from .models import UserProfile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'main_full_name',
        'main_phone_number',
        'main_street_address1',
        'main_street_address2',
        'main_town_or_city',
        'main_county',
        'main_postcode',
        'main_country'
    )

    ordering = ('user',)

admin.site.register(UserProfile, ProfileAdmin)