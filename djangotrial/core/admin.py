from django.contrib import admin
from .models import orders, product

# Register your models here.
admin.site.register(orders)
admin.site.register(product)