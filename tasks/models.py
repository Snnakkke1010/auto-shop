from users.models import Profile
from django.contrib.auth.models import User
from django.db import models


class ProductCategory(models.Model):

    slug = models.SlugField(verbose_name='URL', max_length=255, unique=True, null=True)
    name = models.CharField(verbose_name='Назва категорії', max_length=255, null=True)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name


class Product(models.Model):

    creator = models.ForeignKey(Profile, verbose_name='Автор', null=True, on_delete=models.CASCADE, related_name='product')
    name = models.CharField(verbose_name='Назва продукта', max_length=255, null=True)
    cat = models.ForeignKey(ProductCategory, verbose_name='Категорія', null=True, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Фото подукта', upload_to='product-img/', null=True)
    about = models.TextField(verbose_name='Про продукт', max_length=500, null=True)
    price = models.IntegerField(verbose_name='Ціна', null=True)
    in_stock = models.BooleanField(default=True, null=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'

    def __str__(self):
        return f'Продукт з айді - {self.pk}'