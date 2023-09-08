from django.db import models, connection
from django.utils.timezone import now

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='наименование')
    category_description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('category_name',)

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')
    product_description = models.TextField(verbose_name='описание')
    product_image = models.ImageField(upload_to='media/product/', verbose_name='изображение', **NULLABLE)
    product_category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='категория', **NULLABLE)
    product_purchase_price = models.IntegerField(verbose_name='цена')
    product_date_of_create = models.DateField(verbose_name='дата создания')
    product_last_modified_date = models.DateField(verbose_name='дата изменения', **NULLABLE)

    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('product_name',)

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')

