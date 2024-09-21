from django.db import models

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=30)
    description = models.TextField()
    in_stock = models.BooleanField()

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]