from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name_category = models.CharField(max_length=150, verbose_name="Название категории",)
    description_category = models.TextField(
        **NULLABLE,
        verbose_name="Описание категории",
    )

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name_product = models.CharField(max_length=150, verbose_name="Наименование товара",)
    description_product = models.TextField(verbose_name="Описание товара", **NULLABLE,)
    picture = models.ImageField(
        upload_to="products/", verbose_name="Изображение", **NULLABLE,
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория", related_name="products", **NULLABLE,
    )
    price = models.IntegerField(verbose_name="Цена за покупку",)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания",)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения",
    )
    # manufactured_at = models.DateTimeField(verbose_name="Дата производства продукта", **NULLABLE)

    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
