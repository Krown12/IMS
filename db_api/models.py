from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class category(models.Model):
    categories = (
    ('E', 'Electronics'), 
    ('C', 'Clothing'), 
    ('HK', 'Home and Kitchen'),
    ('B', 'Books'),
    ('S&O', 'Sports and Outdoors'), 
    ('B&PC', 'Beauty and Personal Care'), 
    ('T&G', 'Toys and Games'), 
    ('F', 'Furniture'), 
    ('A', 'Automotive'), 
    ('H&W', 'Health and Wellness'), 
    ('G', 'Grocery'), 
    ('J', 'Jewelry'),
    ("NONE","UNAVIALABLE")
    # Add more categories as needed
    )
    name=models.CharField(max_length=100,choices = categories,default="NONE")
    def __str__(self):
        return self.name
    


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.TextField()
    discount = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ],default = 0)
    category = models.ForeignKey(category,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.name

class user_info(models.Model):
    male ="M"
    female ="F"
    others ='O'
    Gender=((male,"male"),(female,"female"),(others,"others"))
    username = models.CharField(max_length = 55)
    email =  models.EmailField()
    number = models.CharField(max_length=10)
    is_verified = models.BooleanField(default = False)
    gender = models.CharField(choices = Gender,max_length = 1)
    country = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    def __str__(self):
        return self.email
    

