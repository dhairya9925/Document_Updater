from django.db import models

# Create your models here.
class general(models.Model):
    country = models.CharField(max_length=100)
    dialCode = models.CharField(max_length=5)
    image = models.CharField(max_length=100)
    def __str__(self):
        return self.country

class Seller(models.Model):
    userName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    contact = models.IntegerField()
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    companyName = models.CharField(max_length=50)
    gstin = models.CharField(max_length=15)
    storeName = models.CharField(max_length=50)

    def __str__(self):
        return self.name