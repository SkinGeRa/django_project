from django.shortcuts import render
from django.views.generic import DetailView

from catalog.models import Product, Category


def index(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Каталог товаров'
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    return render(request, 'catalog/contact.html')


def home(request):
    return render(request, 'catalog/home.html')


def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object_list': product_item,
        'title': f'Категория товара - {product_item.product_name}'
    }
    return render(request, 'catalog/product.html', context)
