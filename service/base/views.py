from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

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


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class EstablishmentList(generics.ListCreateAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
    pagination_class = CustomPagination


class EstablishmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
