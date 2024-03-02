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
]