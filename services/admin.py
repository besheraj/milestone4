from django.contrib import admin
from .models import Service


# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'image',
        'quizz',
    )

    ordering = ('sku',)


admin.site.register(Service, ServiceAdmin)
