from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_by_category', args=[self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категрия'
        verbose_name_plural = 'Категрии'


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField('Название продукта', max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField('Картинка', upload_to='products/%Y/%m/%d', default='static/no_image.png')
    description = models.TextField('Описание продукта', blank=True)
    price = models.DecimalField('Цена товара', max_digits=10, decimal_places=2)
    sale = models.BooleanField('Скидка', default=False)
    hots = models.BooleanField('Новинки', default=False)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def sale_percent(self):
        if self.sale > 0:
            percent = self.sale * self.price / 100
            return self.price - percent
