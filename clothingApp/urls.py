from django.urls import path
from . import views

urlpatterns = [
    path('product/create/', views.product_create, name='product_create'),
    path('products/', views.products, name='products'),
    path('product/<int:pk>', views.product_details, name='product_details'),

    path('catalog/create/', views.catalog_create, name='catalog_create'),
    path('catalogs/', views.catalogs, name='catalogs'),
    path('catalog/<int:pk>', views.catalog_details, name='catalog_details'),

    path('user/create/', views.user_create, name='user_create'),
    path('users/', views.users, name='users'),
    path('user/<int:pk>', views.user_details, name='user_details'),

    path('order/create/', views.order_create, name='order_create'),
    path('orders/', views.orders, name='orders'),
    path('order/<int:pk>', views.order_details, name='order_details'),
]