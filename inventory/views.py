from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Product


# Sign Up view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Login view
def login (request):
    if request.method=='Post':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate (username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home') 

     
# Home view
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

# Create Product view
def create_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        product = Product(name=name, description=description, price=price)
        product.save()
        return redirect('home')
    return render(request, 'create_product.html')

# Product Details view
def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_details.html', {'product': product})

# Delete Product view
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('home')

# Update Product view
def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.save()
        return redirect('product_details', product_id=product_id)
    return render(request, 'update_product.html', {'product': product})



