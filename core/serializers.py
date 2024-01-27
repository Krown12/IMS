from rest_framework import serializers
# from .models import *
from django.contrib.auth import get_user_model
user = get_user_model()
class loginserializer(serializers.ModelSerializer):
    class Meta:
        model =user
        fields="__all__"
        