
from rest_framework import serializers
from .models import Product,Catalog,User,Order,OrderProductsDetails

class ProductSerializer(serializers.ModelSerializer):
    product_name= serializers.CharField(max_length=200, required=True)
    product_price = serializers.IntegerField()
    product_type=serializers.CharField(max_length=200, required=True)
    warrenty = serializers.BooleanField()
    catalog_id = serializers.PrimaryKeyRelatedField(queryset=Catalog.objects.all(), allow_null=True)

    class Meta:  
        model = Product  
        fields = ('__all__')  

class CatalogSerializer(serializers.ModelSerializer):
    catalog_name= serializers.CharField(max_length=200, required=True)
    catalog_Desc = serializers.CharField(max_length=200, required=True)
    sort_order=serializers.IntegerField()

    class Meta:  
        model = Catalog  
        fields = ('__all__') 


class UserSerializer(serializers.ModelSerializer):
    user_firstname= serializers.CharField(max_length=200, required=True)
    user_lastname= serializers.CharField(max_length=200, required=True)
    user_mailId= serializers.CharField(max_length=200, required=True)
    user_contact= serializers.CharField(max_length=200, required=True)
    user_address= serializers.CharField(max_length=200, required=True)

    class Meta:  
        model = User  
        fields = ('__all__') 


class OrderSerializer(serializers.ModelSerializer):
    products= serializers.IntegerField()
    total_price= serializers.IntegerField()
    discount= serializers.IntegerField()
    user_id= serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=True)
    payment_mode= serializers.CharField(max_length=200, required=True)

    class Meta:  
        model = Order  
        fields = ('__all__') 
 