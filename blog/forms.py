from django import forms

from .models import Post,ProductDetails,Catalog
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