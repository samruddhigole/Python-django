from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from .serializers import ProductSerializer,CatalogSerializer,UserSerializer,OrderSerializer
from .models import Product,Catalog,User,Order
from django.http import HttpResponse,Http404

from rest_framework.views import APIView

class ProductList(APIView):
    def get(self,request,format=None):     # Get all Products
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):    # Create Product
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetails(APIView):
    def get_object(self,pk):
        try: 
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self,request,pk,formate=None):  # Get product by id
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
class CatalogList(APIView):

    def get(self,request,format=None):    # Get all Catalogs
        catalogs = Catalog.objects.all()
        serializer = CatalogSerializer(catalogs,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):    # Create Catalog
        serializer = CatalogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CatalogDetails(APIView):
    def get_object(self,pk):
        try:
            return Catalog.objects.get(pk=pk)
        except:
            raise Http404
    
    def get(self,request,pk,format=None):    #Get catalog by id
        catalog = self.get_object(pk)
        serializer = CatalogSerializer(catalog)
        return Response(serializer.data)


class UserList(APIView):
    def get(self,request,format=None):   # Get all users
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):    # Create User
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDetails(APIView):
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except:
            raise Http404
    
    def get(self,request,pk,format=None):    #Get user by id
        catalog = self.get_object(pk)
        serializer = UserSerializer(catalog)
        return Response(serializer.data)
    
class OrderList(APIView):
    def get(self,request,format=None):   # Get all Orders
        users = Order.objects.all()
        serializer = OrderSerializer(users,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):    # Create Order
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrderDetails(APIView):
    def get_object(self,pk):
        try:
            return Order.objects.get(pk=pk)
        except:
            raise Http404
    
    def get(self,request,pk,format=None):    #Get Order by id
        catalog = self.get_object(pk)
        serializer = OrderSerializer(catalog)
        return Response(serializer.data)

#Product Views
# @api_view(['POST'])
# def product_create(request):
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#     else:  
#         return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
    

# @api_view(['GET'])
# def products(request):
#     if request.method == 'GET':
#         posts = Product.objects.all()
#         serializer = ProductSerializer(posts, many=True)
#         return Response(serializer.data)

# @api_view(['GET'])
# def product_details(request, pk):
#     if request.method == 'GET':
#         try:
#             post = Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = ProductSerializer(post)
#         return Response(serializer.data)

#Catalog Views
# @api_view(['POST'])
# def catalog_create(request):
#     serializer = CatalogSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#     else:  
#         return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
    
# @api_view(['GET'])
# def catalogs(request):
#     if request.method == 'GET':
#         posts = Catalog.objects.all()
#         serializer = CatalogSerializer(posts, many=True)
#         return Response(serializer.data)
    
# @api_view(['GET'])
# def catalog_details(request, pk):
#     if request.method == 'GET':
#         try:
#             post = Catalog.objects.get(pk=pk)
#         except Catalog.DoesNotExist:
#             return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = CatalogSerializer(post)
#         return Response(serializer.data)
    

# #User Views
# @api_view(['POST'])
# def user_create(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#     else:  
#         return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
    
# @api_view(['GET'])
# def users(request):
#     if request.method == 'GET':
#         posts = User.objects.all()
#         serializer = UserSerializer(posts, many=True)
#         return Response(serializer.data)
    
# @api_view(['GET'])
# def user_details(request, pk):
#     if request.method == 'GET':
#         try:
#             post = User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = UserSerializer(post)
#         return Response(serializer.data)

# #Order Views   
# @api_view(['POST'])
# def order_create(request):
#     serializer = OrderSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#     else:  
#         return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
    
# @api_view(['GET'])
# def orders(request):
#     if request.method == 'GET':
#         posts = Order.objects.all()
#         serializer = OrderSerializer(posts, many=True)
#         return Response(serializer.data)
    
# @api_view(['GET'])
# def order_details(request, pk):
#     if request.method == 'GET':
#         try:
#             post = Order.objects.get(pk=pk)
#         except Order.DoesNotExist:
#             return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = OrderSerializer(post)
#         return Response(serializer.data)
    
    



