from django.db import models

# Create your models here.
class Service(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=False)
    quizz = models.URLField(max_length=1024, null=True, blank=False)


    def __str__(self):
        return self.name