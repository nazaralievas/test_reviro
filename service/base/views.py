from rest_framework import generics
from .models import Product, Establishment
from .serializers import ProductSerializer, EstablishmentSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class EstablishmentList(generics.ListCreateAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer


class EstablishmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
