from django.views.generic import ListView
from .models import Product
# Create your views here.

class ProductsList(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'product/list.html'
