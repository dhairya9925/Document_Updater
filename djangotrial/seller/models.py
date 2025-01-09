from django.db import models

# Create your models here.

class Seller(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    contact = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    companyName = models.CharField(max_length=50)
    gstin = models.CharField(max_length=15)
    storeName = models.CharField(max_length=50)
    createOn = models.DateTimeField(auto_now_add=True)
    lastLogin = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

