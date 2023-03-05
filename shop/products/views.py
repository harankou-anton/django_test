import os

from django.shortcuts import render

# Create your views here.
import logging
from django.db.models import Sum, F
from django.http import HttpResponse
from django.conf import settings
from products.models import Product
logger = logging.getLogger(__name__)


def index(request):
    get_all_products = Product.objects.all()
    prod_for_view = ""
    if request.GET.get("title"):
        get_all_products = get_all_products.filter(title=request.GET.get("title"))

    if request.GET.get("color"):
        get_all_products = get_all_products.filter(color__icontains=request.GET.get("color"))

    if request.GET.get("sort") == 'price':
        get_all_products = get_all_products.order_by('-price')
        for_view = '<br>'.join([f'Product name - {data.title}. Price - {data.price}' for data in get_all_products])
        return HttpResponse(f'Products sorted by price <br> {for_view}')

    if request.GET.get("sort") == 'popularity':
        get_all_products = get_all_products.annotate(count_sum=Sum("purchases__count")).order_by('-count_sum')
        for_view = '<br>'.join([f'Product name - {data.title}. Sold - {data.count_sum}' for data in get_all_products])
        return HttpResponse(f'Products sorted by popularity <br> {for_view}')

    if request.GET.get("sort") == 'purchased_money':
        get_all_products = get_all_products.annotate(
            purchased_money=Sum(F('price')*F('purchases__count'))).order_by('-purchased_money')
        for_view = '<br>'.join([f'Product name - {data.title}. Earned - {data.purchased_money}' for data in get_all_products])
        return HttpResponse(f'Products sorted by earned money <br> {for_view}')

    for data in get_all_products:
        get_data = f'Product name - {data.title}. Price - {data.price}.<br>'
        prod_for_view += get_data

    return HttpResponse(prod_for_view)
