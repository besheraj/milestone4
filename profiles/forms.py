from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_photo','main_full_name', 'main_phone_number',
                  'main_street_address1', 'main_street_address2',
                  'main_town_or_city', 'main_postcode', 'main_county',
                  'main_country',)
        labels = {
            'profile_photo': 'Profile Photo',
            'main_full_name': 'Full Name',
            'main_phone_number': 'Phone Number',
            'main_postcode': 'Postal Code',
            'main_town_or_city': 'Town or City',
            'main_street_address1': 'Street Address 1',
            'main_street_address2': 'Street Address 2',
            'main_county': 'County, State or Locality',
            'main_country': 'Country',
        }

