from django.db import models
from core.models import orders, product

# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=100)
    contact = models.IntegerField(unique=True, null=True)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    createOn = models.DateTimeField(auto_now_add=True)
    lastLogin = models.DateTimeField(auto_now=True)


    order = models.ForeignKey(orders, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class cart(models.Model):
    price = models.IntegerField()
    products = models.ForeignKey(product, on_delete=models.CASCADE)