from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm

def index(request):
    products = Product.objects.all()
    context={
        'products':products
    }
    return render(request, 'myapp/index.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context={
        'product': product
    }
    return render(request, 'myapp/product_detail.html', context)

def create_product(request,):
    context={
        'product_form':ProductForm()
        }
    return render(request,'myapp/product_form.html', context)