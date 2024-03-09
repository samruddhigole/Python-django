from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    
class PartyDetails(models.Model):
    party_name = models.CharField(max_length=200)
    general_secretary = models.CharField(max_length=200)
    president = models.CharField(max_length=200)
    headquarters =  models.CharField(max_length=200)

    def __str__(self):
        return self.party_name
    
class ProductDetails(models.Model):
    product_name= models.CharField(max_length=200)
    product_price = models.IntegerField(null=True)
    product_type=models.CharField(max_length=200)
    warrenty = models.BooleanField(null=True)
    catalog_id = models.ForeignKey("Catalog",on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.product_name
    
class Catalog(models.Model):
    # catalog_id = models.IntegerField(null=False)
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

class OrderProductsDetails(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.IntegerField(null=True)
    product_quantity = models.IntegerField(null=True)
    product_id = models.ForeignKey("ProductDetails",on_delete=models.CASCADE,null=True)
    order_id = models.ForeignKey("Order",on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.product_name




