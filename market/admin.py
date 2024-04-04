from django.contrib import admin
from .models import *

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'get_products']

    def get_products(self, category):
        return category.products.all()


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'get_category']

    def get_category(self, product):
        return [category.name for category in product.category.all()]

admin.site.register(Shop)

admin.site.register(Mark)

admin.site.register(Imgs)