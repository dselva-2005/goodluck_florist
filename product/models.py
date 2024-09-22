from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
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
    
    def get_absolute_url(self):
        return reverse("product:product_detail", args=[self.pk])
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    publish = models.DateField(default=timezone.now)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    active = models.BooleanField()


class Review(models.Model):
    class Rating(models.IntegerChoices):
        POOR = 1, 'Poor'
        FAIR = 2, 'Fair'
        GOOD = 3, 'Good'
        VERY_GOOD = 4, 'Very Good'
        EXCELLENT = 5, 'Excellent'

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=Rating.choices,default=Rating.EXCELLENT)
    comment = models.TextField()
    created = models.DateField(auto_now_add=True)