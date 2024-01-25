from rest_framework import serializers
from .models import *
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields  = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    category_details = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields  = ('name','price','description','discount','category_details',)



