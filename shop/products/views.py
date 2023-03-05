import os

from django.shortcuts import render

# Create your views here.
import logging
from django.http import HttpResponse
from django.conf import settings
from products.models import Product
logger = logging.getLogger(__name__)


def index(request):
    get_all_products = Product.objects.all()
    prod_for_view = ""
    if request.GET.get("title"):
        get_all_products = get_all_products.filter(title=request.GET.get("title"))

    if request.GET.get("purchases__count"):
        get_all_products = get_all_products.filter(purchases__count=request.GET.get("purchases__count"))

    if request.GET.get("color"):
        get_all_products = get_all_products.filter(color__icontains=request.GET.get("color"))

    for data in get_all_products:
        get_data = f'Product name - {data.title}. Price - {data.price}.<br>'
        prod_for_view += get_data

    return HttpResponse(prod_for_view)