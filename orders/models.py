from django.db import models
from django.contrib.auth.models import User
import secrets
import string

def generate_random_id(length=8):
    characters = string.ascii_letters + string.digits  # alphanumeric characters
    return ''.join(secrets.choice(characters) for _ in range(length))

# Create your models here.
class OrderModel(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order_number = models.CharField(default=generate_random_id(10))
    created = models.DateTimeField(auto_now_add=True)