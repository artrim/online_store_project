from django.contrib import admin

from catalog.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "name_product", "price", "category",)
    list_filter = ("category",)
    search_fields = ("name_product", "description_product",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name_category",)
