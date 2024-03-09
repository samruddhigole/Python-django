from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    path('post/products/', views.product_list, name='product_list'),
    path('post/product/<int:pk>/', views.product_detail, name='product_detail'),
    path('post/product/new/',views.product_new,name='product_new'),
    
    path('post/catalogs/', views.catalog_list, name='catalog_list'),
    path('post/catalog/new/',views.catalog_new,name='catalog_new'),
    path('post/catalog/<int:pk>/', views.catalog_detail, name='catalog_detail'),

    path('user/new',views.user_new, name='user_new'),
    path('user/details/<int:pk>/',views.user_details, name='user_details'),
    path('users/', views.user_list, name='user_list'),

    path('order/new',views.order_new, name='order_new'),
    path('order/details/<int:pk>/',views.order_details, name='order_details'),
    path('order/products', views.order_products_details, name='order_products_details'),



]