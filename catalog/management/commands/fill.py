from datetime import datetime
from random import randint

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):

        Category.truncate()
        Product.truncate()

        categories_list = [
            {'pk': 1, 'category_name': 'Овощи', 'category_description': 'По оптовой цене, сочные и свежие.'},
            {'pk': 2, 'category_name': 'Электроника',
             'category_description': 'Импортная, быстрая, мощная и недорогая.'},
        ]

        categories_for_create = []
        for category in categories_list:
            categories_for_create.append(
                Category(**category)
            )
        Category.objects.bulk_create(categories_for_create)

        products_for_create = []
        products_list = [
            {"product_name": "Ноутбук", "product_description": "Мощный, быстрый, недорогой", "product_image": "",
             "product_category": categories_for_create[1], "product_purchase_price": randint(5000, 100000),
             "product_date_of_create": datetime.now(), "product_last_modified_date": datetime.now(),
             },
            {"product_name": "Баклажан", "product_description": "Спелый и сочный", "product_image": "",
             "product_category": categories_for_create[0], "product_purchase_price": randint(50, 100),
             "product_date_of_create": datetime.now(), "product_last_modified_date": datetime.now(),
             },
            {"product_name": "Помидоры", "product_description": "Похож на овощ, но это фрукт", "product_image": "",
             "product_category": categories_for_create[0], "product_purchase_price": randint(50, 100),
             "product_date_of_create": datetime.now(), "product_last_modified_date": datetime.now(),
             },
            {"product_name": "Пылесос", "product_description": "Сосет лучше всех", "product_image": "",
             "product_category": categories_for_create[1], "product_purchase_price": randint(5000, 100000),
             "product_date_of_create": datetime.now(), "product_last_modified_date": datetime.now(),
             },
            {"product_name": "Картофель", "product_description": "Любим в Беларуси", "product_image": "",
             "product_category": categories_for_create[0], "product_purchase_price": randint(50, 100),
             "product_date_of_create": datetime.now(), "product_last_modified_date": datetime.now(),
             },
        ]
        for product in products_list:
            products_for_create.append(Product(**product))

        Product.objects.bulk_create(products_for_create)
