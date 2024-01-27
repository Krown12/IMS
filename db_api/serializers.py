from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields  = ['name','id']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields  = ['name','price','description','discount','category']

# class User(serializers.ModelSerializer):
#     class Meta:
#         model = user
#         fields = "__all__"

