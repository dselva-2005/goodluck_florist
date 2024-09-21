from django.urls import path
from . import views


app_name = 'product'

urlpatterns = [
    path('',views.ProductsList.as_view(),name='product_list'),
]
