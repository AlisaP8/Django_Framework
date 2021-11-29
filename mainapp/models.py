from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='название', max_length=64, unique=True)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('-id',)


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='категория')
    name = models.CharField(verbose_name='название', max_length=128)
    image = models.ImageField(upload_to='products', blank=True, verbose_name='картинка')
    short_desc = models.CharField(verbose_name='краткое описание', max_length=255)
    description = models.TextField(verbose_name='описание')
    price = models.DecimalField(verbose_name='цена', max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveSmallIntegerField(verbose_name='количество', default=0)

    def __str__(self):
        return f'{self.name} ({self.category.name})'


