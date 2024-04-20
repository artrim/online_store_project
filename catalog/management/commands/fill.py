import json

from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('catalog_data.json') as file:
            fixture = json.load(file)
            command_list = []
            for item in fixture:
                if item['model'] == "catalog.category":
                    command_list.append(item)
            return command_list

    @staticmethod
    def json_read_products():
        with open('catalog_data.json') as file:
            fixture = json.load(file)
            command_list = []
            for item in fixture:
                if item['model'] == "catalog.product":
                    command_list.append(item)
            return command_list

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(id=category['pk'], name_category=category['fields']['name_category'],
                         description_category=category['fields']['description_category'])
            )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(id=product['pk'], category=Category.objects.get(pk=product['fields']['category']),
                        name_product=product['fields']['name_product'], price=product['fields']['price'],
                        description_product=product['fields']['description_product'])
            )

        Product.objects.bulk_create(product_for_create)
