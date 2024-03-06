from django.db import models
from django.conf import settings

class Product(models.Model):
    product_name= models.CharField(max_length=200)
    product_price = models.IntegerField(null=True)
    product_type=models.CharField(max_length=200)
    warrenty = models.BooleanField(null=True)
    catalog_id = models.ForeignKey("Catalog",on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.product_name
    
class Catalog(models.Model):
    catalog_name = models.CharField(max_length=200)
    catalog_Desc = models.CharField(max_length=200)
    sort_order = models.IntegerField(null=True)

    def __str__(self):
        return self.catalog_name
    
class User(models.Model):
    user_firstname = models.CharField(max_length=200)
    user_lastname = models.CharField(max_length=200)
    user_mailId = models.CharField(max_length=200)
    user_contact = models.CharField(max_length=200)
    user_address = models.CharField(max_length=200)

    def __str__(self):
        return self.user_mailId
    
class Order(models.Model):
    products = models.IntegerField(null=True)
    total_price = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    user_id = models.ForeignKey("User",on_delete=models.CASCADE,null=True)
    payment_mode = models.CharField(max_length=200)

    def __str__(self):
        return self.products
    