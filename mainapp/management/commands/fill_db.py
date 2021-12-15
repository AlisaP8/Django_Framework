from django.conf import settings
from django.core.management.base import BaseCommand

from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory
from django.contrib.auth.models import User
import json


def load_from_json(file_name):
    with open(f"{settings.BASE_DIR}/json/{file_name}.json", encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            ProductCategory.objects.create(**category)

        products = load_from_json('products')
        for product in products:
            category_name = product['category']
            category_item = ProductCategory.objects.get(name=category_name)
            product['category'] = category_item
            Product.objects.create(**product)

        ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=18)

