import uuid

from django.db.models.signals import post_save
from django.utils.text import slugify
from django.dispatch import receiver
from django.db import models
from account.models import User


def product_image_path(Product, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    # return 'product_{0}/{1}'.format(image.product.id, filename)
    return f'images/category/product_{Product.name}/{filename}'


class Category(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class Mark(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ManyToManyField(Category, related_name='products')
    img = models.ImageField(upload_to=product_image_path)
    discount = models.IntegerField(default=0)
    discounted_price = models.IntegerField()
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, null=True, blank=True, default=10, related_name='marks')
    inventory_range = models.IntegerField(default=20)
    inventory = models.BooleanField(default=True)

    @property
    def discounted_price(self):
        original_price = self.price
        discounted_price = original_price - (original_price * self.discount / 100)

        if self.inventory_range == 0:
            x = self.inventory = True

        return int(discounted_price)



class Shop(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.TextField()
    deta = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product} ---- {self.user}'


class Imgs(models.Model):
    img_1 = models.ImageField(upload_to='imges/')
    img_2 = models.ImageField(upload_to='imges/')
    takfif = models.ForeignKey(Product, on_delete=models.CASCADE)
    baner_1 = models.ImageField(upload_to='imges/')
    baner_2 = models.ImageField(upload_to='imges/')
