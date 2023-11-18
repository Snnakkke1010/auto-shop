from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/add/', add_product, name='add_product'),
]