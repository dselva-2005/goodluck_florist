from django.contrib import admin
from .models import Product,Comment,Review
# Register your models here.

@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name','description','in_stock']
    list_filter = ['name','in_stock']
    search_fields = ['name']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','active','created']
    list_filter = ['user','active']
    search_fields = ['user']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['rating','comment','created']
    list_filter = ['rating','created']
    search_fields = ['comment']