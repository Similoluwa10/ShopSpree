from django.db import models
from user.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='category_imgs')
    slug = models.SlugField(blank=True)
    
    class Meta:
        db_table = 'homepage_category'  


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=255)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='product_imgs')
    slug = models.SlugField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'homepage_product'

    
# class Cart(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
#     product = models.ManyToManyField(Product)
    
#     class Meta:
#         db_table = 'homepage_cart'
