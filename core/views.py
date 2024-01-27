from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .serializers import loginserializer
# Create your views here.
user= get_user_model()
# @api_view(['POST'])
# def login(request,pk=None):
#     data = request.data
#     username = data.get('email')
#     password = data.get('password')
#     user = authen

