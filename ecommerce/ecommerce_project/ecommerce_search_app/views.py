from django.http import HttpResponse
from django.shortcuts import render
from ecommerce_app . models import Product
from django.db.models import Q


def SearchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(product_name__contains=query) | Q(product_desc__contains=query))
        context = {
            'query': query,
            'products': products
        }
    return render(request,'search.html', context)

