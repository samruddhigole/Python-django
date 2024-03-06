from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from .serializers import ProductSerializer,CatalogSerializer,UserSerializer,OrderSerializer
from .models import Product,Catalog,User,Order
from django.http import HttpResponse

#Product Views
@api_view(['POST'])
def product_create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:  
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
    

@api_view(['GET'])
def products(request):
    if request.method == 'GET':
        posts = Product.objects.all()
        serializer = ProductSerializer(posts, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def product_details(request, pk):
    if request.method == 'GET':
        try:
            post = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(post)
        return Response(serializer.data)


#Catalog Views
@api_view(['POST'])
def catalog_create(request):
    serializer = CatalogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:  
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
    
@api_view(['GET'])
def catalogs(request):
    if request.method == 'GET':
        posts = Catalog.objects.all()
        serializer = CatalogSerializer(posts, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def catalog_details(request, pk):
    if request.method == 'GET':
        try:
            post = Catalog.objects.get(pk=pk)
        except Catalog.DoesNotExist:
            return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CatalogSerializer(post)
        return Response(serializer.data)
    

#User Views
@api_view(['POST'])
def user_create(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:  
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
    
@api_view(['GET'])
def users(request):
    if request.method == 'GET':
        posts = User.objects.all()
        serializer = UserSerializer(posts, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def user_details(request, pk):
    if request.method == 'GET':
        try:
            post = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(post)
        return Response(serializer.data)

#Order Views   
@api_view(['POST'])
def order_create(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:  
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
    
@api_view(['GET'])
def orders(request):
    if request.method == 'GET':
        posts = Order.objects.all()
        serializer = OrderSerializer(posts, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def order_details(request, pk):
    if request.method == 'GET':
        try:
            post = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OrderSerializer(post)
        return Response(serializer.data)
    
    



