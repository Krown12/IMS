from django.db import models
from django.contrib.auth.models import AbstractUser
from .customeobjects import User_custom_manager

# Create your models here.
class CustomUser(AbstractUser):
    username=models.CharField(max_length=55)
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

 
    objects=User_custom_manager()
    
    
    
 
    