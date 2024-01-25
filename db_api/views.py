from django.shortcuts import render
from .serializers import *
from rest_framework.viewsets import ModelViewSet 
from .models import *
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class CategoryCURD(ModelViewSet):
    queryset = category.objects.all()
    serializer_class=CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields  = ['name']
class ProductCURD(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields  = ['category_id']
    
