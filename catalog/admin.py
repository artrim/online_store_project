from django.contrib import admin

from catalog.models import Product, Category, Blog, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("pk", "name_product", "price", "category",)
    list_filter = ("category",)
    search_fields = ("name_product", "description_product",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name_category",)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "is_published", "preview",)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product', 'number_version', 'name_version', 'is_active',)
