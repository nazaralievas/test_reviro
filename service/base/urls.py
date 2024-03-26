from django.urls import path
from .views import *


urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<str:pk>/', ProductDetail.as_view(), name='product-detail'),
    
    path('establishments/', EstablishmentList.as_view(), name='establishment-list'),
    path('establishments/<str:pk>/', EstablishmentDetail.as_view(), name='establishment-detail'),
]
