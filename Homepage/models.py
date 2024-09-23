from django.db import models


class ProductGroup(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255, null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=255)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=255, null=True, blank=True)

