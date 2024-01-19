from django.db import models

# Create your models here.

class category(models.Model):
    categories = (
    ("Electronics", "E"),
    ("Clothing", "C"),
    ("Home and Kitchen", "HK"),
    ("Books", "B"),
    ("Sports and Outdoors", "S&O"),
    ("Beauty and Personal Care", "B&PC"),
    ("Toys and Games", "T&G"),
    ("Furniture", "F"),
    ("Automotive", "A"),
    ("Health and Wellness", "H&W"),
    ("Grocery", "G"),
    ("Jewelry", "J"),
    # Add more categories as needed
    )
    name=models.CharField(max_length=10,options = categories)


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.TextField()
    discount = models.IntegerField(max_value = 100)
    category_id = models.ForeignKey(on_delete=models.SET_NULL)

class user(models.Model):
    male ="M"
    female ="F"
    others ='O'
    Gender=((male,"male"),(female,"female"),(others,"others"))
    username = models.CharField(max_length = 55)
    email =  models.EmailField()
    number = models.CharField(max_length=10)
    is_verified = models.BooleanField(default = False)
    gender = models.CharField(options = Gender,max_length = 1)
    country = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    
