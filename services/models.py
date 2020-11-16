from django.db import models


class Service(models.Model):
    # quizz elements
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField(null=True, blank=False)
    quizz = models.URLField(max_length=1024, null=True, blank=False)

    def __str__(self):
        return self.name
