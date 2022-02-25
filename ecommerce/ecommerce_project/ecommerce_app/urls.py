from django.urls import path
from . import views
app_name = 'ecommerce_app'
urlpatterns = [
    path('', views.allProductCat, name='allProductCat'),
    path('<slug:c_slug>/', views.allProductCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/', views.productDetail, name='product_category_detail'),
]