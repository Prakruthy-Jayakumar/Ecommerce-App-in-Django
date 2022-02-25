from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import  Paginator, EmptyPage, InvalidPage

def allProductCat(request, c_slug=None):
    c_page = None
    products_list = None
    if c_slug != None:
        c_page = get_object_or_404(Category, category_slug = c_slug)
        products_list = Product.objects.all().filter(product_category = c_page, product_availability = True)
    else:
        products_list = Product.objects.all().filter(product_availability = True)
    #     PAGINATOR CODE below and in category page also
    paginator = Paginator(products_list, 6)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    #     PAGE FOR EMPTY AND INVALID PAGE
    try:
        products = paginator.page(page)
    except (EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request,'category.html',{'category':c_page, 'products':products})


def productDetail(request,c_slug, p_slug):
    try:
        product = Product.objects.get(product_category__category_slug = c_slug, product_slug = p_slug)
    except Exception as e:
        raise e

    return render(request,'product.html',{'product':product})