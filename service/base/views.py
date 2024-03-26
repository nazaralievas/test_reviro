from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Establishment
from .serializers import ProductSerializer, EstablishmentSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Product List':'/product-list/',
        'Product Detail':'/product-detail/',
        'Establishment List':'/establishment-list/',
        'Establishment Detail':'/establishment-detail/',
        }
    return Response(api_urls)


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
