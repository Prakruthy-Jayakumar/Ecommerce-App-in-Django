from django.contrib import admin
from . models import Category, Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'category_slug']
    prepopulated_fields = {'category_slug':('category_name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price','product_stock','product_availability','product_create_time','product_updated']
    list_editable = ['product_price','product_stock','product_availability']
    prepopulated_fields = {'product_slug':('product_name',)}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)