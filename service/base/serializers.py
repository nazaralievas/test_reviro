from rest_framework import serializers
from .models import Product, Establishment


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity', 'created', 'updated']
        read_only_fields = ['id', 'created', 'updated']


class EstablishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishment
        fields = ['id', 'name', 'description', 'location', 'working_hours', 'created', 'updated']
        read_only_fields = ['id', 'created', 'updated']
