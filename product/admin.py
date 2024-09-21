from django.contrib import admin
from .models import Product
# Register your models here.

@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name','description','in_stock']
    list_filter = ['name','in_stock']
    search_fields = ['name']