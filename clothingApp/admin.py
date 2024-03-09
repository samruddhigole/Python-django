from django.contrib import admin
from .models import Product,Catalog,User,Order

admin.site.register(Product)
admin.site.register(Catalog)
admin.site.register(User)
admin.site.register(Order)