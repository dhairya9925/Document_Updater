from django.db import models
from seller.models import Seller
from consumer.models import users

# Create your models here.
class countryCode(models.Model):
    country = models.CharField(max_length=100)
    dialCode = models.CharField(max_length=5)
    image = models.CharField(max_length=100)
    def __str__(self):
        return self.country
    
class product(models.Model):
    category = [
        ("t", "toys")
    ]
    productName = models.CharField(max_length=250)
    price = models.IntegerField()
    stock = models.IntegerField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    description = models.TextField()
    productCategory = models.CharField( max_length=1, choices=category, default='t')
    
    def __str__(self):
        return self.productName
    

class orders(models.Model):
    status = [
        ("p", "pending") ,
        ("s", "shipped") ,
        ("d", "delivered") ,
        ("c", "canceled") ,
    ]
    price = models.IntegerField()
    quantity = models.IntegerField()
    buyer = models.ForeignKey(users, on_delete=models.CASCADE)
    description = models.TextField()
    orderDate = models.DateTimeField(auto_now_add=True, blank=True)
    orderStatus = models.CharField( max_length=1, choices=status, default='p')

    def __str__(self):
        return self.productName
