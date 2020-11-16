from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('main_full_name','main_phone_number',
                  'main_street_address1', 'main_street_address2',
                  'main_town_or_city', 'main_postcode', 'main_country',
                  'main_county',)

    def __init__(self, *args, **kwargs):

        # add place holders
        super().__init__(*args, **kwargs)
        placeholders = {
            'main_full_name' : 'full_name',
            'main_phone_number': 'Phone Number',
            'main_postcode': 'Postal Code',
            'main_town_or_city': 'Town or City',
            'main_street_address1': 'Street Address 1',
            'main_street_address2': 'Street Address 2',
            'main_country': 'Country',
            'main_county': 'County, State or Locality',
        }
        # exempt country from having place holder and adding classes
        for field in self.fields:
            if field != 'main_county':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder