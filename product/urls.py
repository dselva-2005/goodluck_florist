from django.urls import path
from . import views


app_name = 'product'

urlpatterns = [
    path('',views.ProductsList.as_view(),name='product_list'),
    path('<int:pk>/',views.ProductsDetailView.as_view(),name='product_detail'),
    path('<int:product_id>/review',views.add_review,name='add_product_review'),
    path('search/',views.prduct_search,name='product_search'),
]
