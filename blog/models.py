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
