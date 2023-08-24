from datetime import datetime
from random import randint

from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {'product_name': 'Ноутбук', 'product_description': 'Мощный, быстрый, недорогой',
             'product_category': 'Электроника', 'product_purchase_price': randint(50, 100),
             'product_date_of_create': datetime.now(), 'product_last_modified_date': datetime.now()},
            {'product_name': 'Баклажан', 'product_description': 'Спелый и сочный',
             'product_category': 'Овощи', 'product_purchase_price': randint(50, 100),
             'product_date_of_create': datetime.now(), 'product_last_modified_date': datetime.now()},
            {'product_name': 'Помидоры', 'product_description': 'Похож на овощ, но это фрукт',
             'product_category': 'Овощи', 'product_purchase_price': randint(50, 100),
             'product_date_of_create': datetime.now(), 'product_last_modified_date': datetime.now()},
            {'product_name': 'Пылесос', 'product_description': 'Сосет лучше всех',
             'product_category': 'Электроника', 'product_purchase_price': randint(50, 100),
             'product_date_of_create': datetime.now(), 'product_last_modified_date': datetime.now()},
            {'product_name': 'Картофель', 'product_description': 'Любим в Беларуси',
             'product_category': 'Овощи', 'product_purchase_price': randint(50, 100),
             'product_date_of_create': datetime.now(), 'product_last_modified_date': datetime.now()}
        ]
        product_for_create = []
        Product.objects.all().delete()
        for product_item in product_list:
            product_for_create.append(Product(**product_item))
        Product.objects.bulk_create(product_for_create)
