from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length= 200, null = True)
    phone= models.CharField(max_length= 200, null = True)
    email = models.CharField(max_length= 200, null = True)
    date_created= models.DateTimeField(auto_now_add= True, null = True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY= (
        ("Cheese Pizza", "Cheese Pizza"),
        ("Pepperoni Pizza", "Pepperoni Pizza"),
        ("Sausage Pizza", "Sausage Pizza"),
        ("Meat Lover Pizza", "Meat Lover Pizza"),
        ("Hawaiian Pizza", "Hawaiian Pizza"),
        
    )

    
    price= models.FloatField(null= True)
    category= models.CharField(max_length= 200, null = True, choices= CATEGORY)
    
    date_created= models.DateTimeField(auto_now_add= True, null = True)

    def __str__(self):
        return self.category

class Order(models.Model):
    PAYMENT= (
        ("Card", "Card"),
        ("Cash", "Cash")
    )


    customer= models.ForeignKey(Customer, null=True, on_delete= models.CASCADE)
    product= models.ForeignKey(Product, null=True, on_delete= models.CASCADE)
    date_created= models.DateTimeField(auto_now_add= True, null = True)
    payment = models.CharField(max_length= 200, null = True, choices = PAYMENT)

    def __str__(self):
        return self.customer.name

class Transaction(models.Model):
    customer= models.ForeignKey(User, null=True, on_delete= models.CASCADE)
    deposit = models.DecimalField(decimal_places=2, max_digits=4)
    date = models.CharField(max_length=10)