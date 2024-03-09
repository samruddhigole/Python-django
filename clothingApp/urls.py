from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('product/create/', views.product_create, name='product_create'),
    # path('products/', views.products, name='products'),
    # path('product/<int:pk>', views.product_details, name='product_details'),

    # path('catalog/create/', views.catalog_create, name='catalog_create'),
    # path('catalogs/', views.catalogs, name='catalogs'),
    # path('catalog/<int:pk>', views.catalog_details, name='catalog_details'),

    # path('user/create/', views.user_create, name='user_create'),
    # path('users/', views.users, name='users'),
    # path('user/<int:pk>', views.user_details, name='user_details'),

    # path('order/create/', views.order_create, name='order_create'),
    # path('orders/', views.orders, name='orders'),
    # path('order/<int:pk>', views.order_details, name='order_details'),

    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>',views.ProductDetails.as_view()),

    path('catalogs/', views.CatalogList.as_view()),
    path('catalogs/<int:pk>',views.CatalogDetails.as_view()),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>',views.UserDetails.as_view()),

    path('orders/', views.OrderList.as_view()),
    path('orders/<int:pk>',views.OrderDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)