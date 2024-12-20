from django.db import models


class ProductGroup(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255, null=True, blank=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=255)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=30, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return self.username

    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    product = models.ManyToManyField(Product)
