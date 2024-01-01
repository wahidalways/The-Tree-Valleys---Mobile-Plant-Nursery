from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Customer,Product
from django.db import models

# Create your views here.
def index(request):
    return render(request, 'index.html')
def products(request):
    return render(request, 'products.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')
def about(request):
    return render(request, 'about.html')

def register(request):
    if request.method == 'POST':
        user = Customer(username=request.POST['username'], 
                        password=request.POST['password'], 
                        name=request.POST['name'],email=request.POST['email'])
        user.save()
        return redirect('products')    

def checkSignin(request):
    if request.method == 'POST':
        if Customer.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            customer = Customer.objects.get(username=request.POST['username'], password=request.POST['password'])
            global cs
            def cs():
                return customer.id
            return redirect(products)
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html', context)


def addToCart(request,pname,amt):
    customer = cs()
    pd = Product(cid = customer,pname=pname,amt=amt)
    pd.save()
    return render(request, 'products.html')

def cart(request):
    customer = cs()
    product = Product.objects.filter(cid = customer)
    context = {'pall': product}
    return render(request, 'cart.html', context)


def contact(request):
    return render(request, 'contact.html')