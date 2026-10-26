from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='category_imgs')
    slug = models.SlugField(blank=True)
    
    class Meta:
        db_table = 'homepage_category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='product_imgs')
    slug = models.SlugField(blank=True)
    categories = models.ManyToManyField(
        Category,
        blank=True,
        related_name='products',
    )
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'homepage_product'
