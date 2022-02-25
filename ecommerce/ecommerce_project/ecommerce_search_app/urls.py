from django.urls import path
from . import views

app_name = 'ecommerce_search_app'
urlpatterns = [
    path('', views.SearchResult, name='SearchResult'),
 ]