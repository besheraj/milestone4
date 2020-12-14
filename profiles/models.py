from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    # user profile form
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(null=True, blank=True)
    main_full_name = models.CharField(max_length=20, null=True, blank=False)
    main_phone_number = models.CharField(max_length=20, null=True, blank=False)
    main_street_address1 = models.CharField(max_length=80, null=True, blank=False)
    main_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    main_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    main_county = models.CharField(max_length=80, null=True, blank=False)
    main_postcode = models.CharField(max_length=20, null=True, blank=False)
    main_country = CountryField(blank_label='Country', null=True, blank=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    # create or update profile
    if created:
        UserProfile.objects.create(user=instance).save()
