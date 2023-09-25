from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='страна')
    key = models.IntegerField(verbose_name='ключ', **NULLABLE)
    is_active = models.BooleanField(verbose_name='признак верификации', default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
