from django.shortcuts import redirect
from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post,ProductDetails,Catalog,User,Order,OrderProductsDetails
from .forms import PostForm,ProductForm,CatalogForm,UserForm,OrderForm,OrderProductsDetailsForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    # post = get_object_or_404(Post, pk=pk)
    # Post.objects.get(pk=pk)
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    # form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

#PRODUCTS operations

def product_list(request):
    posts = ProductDetails.objects.all()
    return render(request, 'blog/product_list.html', {'posts': posts})


def product_detail(request, pk):
    post = get_object_or_404(ProductDetails, pk=pk)
    return render(request, 'blog/product_detail.html', {'post': post})


def product_new(request):
    if request.method =="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('product_detail',pk=post.pk)
    else:
        form = ProductForm()
    return render(request, 'blog/product_detail.html', {'form': form})


#CATALOG Operations

def catalog_list(request):
    posts = Catalog.objects.all()
    return render(request, 'blog/catalog_list.html', {'posts': posts})

def catalog_detail(request, pk):
    post = get_object_or_404(Catalog, pk=pk)
    return render(request, 'blog/catalog_detail.html', {'post': post})


def catalog_new(request):
    if request.method =="POST":
        form = CatalogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('catalog_detail', pk=post.pk)
    else:
        form = CatalogForm()
    return render(request, 'blog/catalog_new.html', {'form': form})


#USERS Operations

def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('user_details',pk=post.pk)
    else:
        form = UserForm()
    return render(request,'blog/user_new.html',{'form':form})

def user_details(request, pk):
    post = get_object_or_404(User, pk=pk)
    return render(request, 'blog/user_details.html', {'post': post})

def user_list(request):
    posts = User.objects.all()
    return render(request, 'blog/user_list.html', {'posts': posts})


#ORDERS Operations

def order_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('order_details',pk=post.pk)
    else:
        form = OrderForm()
    return render(request,'blog/order_new.html',{'form':form})

def order_details(request, pk):
    post = get_object_or_404(Order, pk=pk)
    return render(request, 'blog/order_details.html', {'post': post})

def order_products_details(request):
    posts = OrderProductsDetails.objects.all()
    return render(request, 'blog/order_products_details.html', {'posts': posts})





