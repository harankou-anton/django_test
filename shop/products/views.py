import os

from django.shortcuts import render

# Create your views here.
import logging
from django.http import HttpResponse
from django.conf import settings
from products.models import Product
logger = logging.getLogger(__name__)


def index(request):
    # if request.GET.get("param"):
    #     logger.info(f'Custom var = {settings.MY_CUSTOM_VARAIBLE}')
    #     logger.info(f'Custom env var = {settings.MY_ENV_VARAIBLE}')
    #     logger.info(f"My param = {request.GET.get('param')}")
    #
    # if int(os.getenv(key='FIRST_ENV_PARAM')) % 2 != 0:
    #     logger.info(f'first environment variable is {os.getenv(key="SECOND_ENV_PARAM")}')
    # else:
    #     logger.info(f'first environment variable is {os.getenv(key="THIRD_ENV_PARAM")}')

    if request.GET.get("title"):
        get_by_title = Product.objects.filter(title=request.GET.get("title")).first()
        if get_by_title:
            return HttpResponse(f'Product name - {get_by_title.title}. Price - {get_by_title.price}')
        else:
            return HttpResponse('No such product')

    get_all_products = Product.objects.all()
    prod_for_view = ""
    for data in get_all_products:
        get_data = f'Product name - {data.title}. Price - {data.price}\n'
        prod_for_view += get_data
    return HttpResponse(prod_for_view, content_type="text/plain")

