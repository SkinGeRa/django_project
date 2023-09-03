from django.shortcuts import render
from django.views.generic import DetailView

from catalog.models import Product, Category


def index(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Каталог товаров'
    }
    return render(request, 'catalog/product.html', context)


def contacts(request):
    return render(request, 'catalog/contact.html')


def home(request):
    return render(request, 'catalog/home.html')


