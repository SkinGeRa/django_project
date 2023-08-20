from django.shortcuts import render


# Create your views here.
def contacts(request):
    return render(request, 'catalog/contact.html')


def home(request):
    return render(request, 'catalog/home.html')
