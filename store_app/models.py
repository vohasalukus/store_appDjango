from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100
    )
    slug = models.SlugField(
        unique=True
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(
        max_length=100
    )
    address = models.CharField(
        max_length=100
    )
    slug = models.SlugField(
        unique=True
    )

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        ordering = ['id']

    def __str__(self):
        return f'{self.name} {self.address}'


class Product(models.Model):
    name = models.CharField(
        max_length=255
    )
    price = models.FloatField(
        default=0
    )
    quantity = models.IntegerField(
        default=0
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='products'
    )
    store = models.ManyToManyField(
        'Store',
        related_name='products'
    )
    slug = models.SlugField(
        unique=True
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['id']

    def __str__(self):
        return f'{self.name} {self.price} {self.quantity}'

