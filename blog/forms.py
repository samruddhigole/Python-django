from django import forms

from .models import Post,ProductDetails,Catalog,User,Order,OrderProductsDetails
# from .models import

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductDetails
        fields = ('product_name','product_price','product_type','warrenty','catalog_id')

class CatalogForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = ('catalog_name','catalog_Desc','sort_order',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('user_firstname','user_lastname','user_mailId','user_contact','user_address')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('products','total_price','discount','user_id','payment_mode')

class OrderProductsDetailsForm(forms.ModelForm):
    class Meta:
        model = OrderProductsDetails
        fields = ('product_name','product_price','product_quantity','product_id','order_id')