from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='наименование')
    category_description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.category_name} {self.category_description}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('category_name',)


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')
    product_description = models.TextField(verbose_name='описание')
    product_image = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    product_category = models.CharField(max_length=30, verbose_name='категория')
    product_purchase_price = models.IntegerField(verbose_name='цена')
    product_date_of_create = models.DateField(verbose_name='дата создания')
    product_last_modified_date = models.DateField(verbose_name='дата изменения', **NULLABLE)

    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('product_name',)

