from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, index

app_name = CatalogConfig.name

urlpatterns = [
    path('', home),
    path('product/', index),
    path('contacts/', contacts)
]