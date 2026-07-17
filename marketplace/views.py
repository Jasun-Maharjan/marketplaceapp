from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'extending/home.html', {'products': products})

def index(request):
    return HttpResponse("This is Products Page")