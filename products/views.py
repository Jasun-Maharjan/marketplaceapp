from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Category, Product
# Create your views here.

def index(request):
    return HttpResponse("This is Products Page")

def product_detail(request, id):
    product = get_object_or_404(Product, id = id)
    return render(request, 'products/dettails.html',{'product': product})

def products(request):
    return render(request, 'products/details.html')
