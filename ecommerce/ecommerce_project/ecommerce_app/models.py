from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=250, unique=True)
    category_slug = models.SlugField(max_length=250, unique=True)
    category_desc = models.TextField(blank=True)
    category_img = models.ImageField(upload_to='Category Gallery',blank=True)

    class Meta:
        ordering = ('category_name',)
        verbose_name= 'category_name'
        verbose_name_plural= 'categories'

    def get_url(self):
        return reverse('ecommerce_app:products_by_category', args=[self.category_slug])

    def __str__(self):
        return '{}'.format(self.category_name)

class Product(models.Model):
    product_name = models.CharField(max_length=250, unique=True)
    product_slug = models.SlugField(max_length=250, unique=True)
    product_desc = models.TextField(blank=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_img = models.ImageField(upload_to='Product Gallery',blank=True)
    product_stock = models.IntegerField()
    product_availability = models.BooleanField(default=True)
    product_create_time = models.DateTimeField(auto_now_add=True)
    product_updated = models.DateTimeField(auto_now_add=True)

    def get_url(self):
        return reverse('ecommerce_app:product_category_detail',args=[self.product_category.category_slug,self.product_slug])

    def __str__(self):
        return '{}'.format(self.product_name)

    class Meta:
        ordering = ('product_name',)
        verbose_name= 'product'
        verbose_name_plural= 'products'


    def __str__(self):
        return '{}'.format(self.product_name)




