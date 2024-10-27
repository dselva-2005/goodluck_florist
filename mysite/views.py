from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def shop(request):
    return render(request,'shop.html')

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def products(request):
    return render(request,'product-details.html')