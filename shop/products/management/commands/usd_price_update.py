from decimal import Decimal

import requests
from django.core.management.base import BaseCommand
from django.db.models import F
from django_rq import job
from products.models import Product
import logging

logger = logging.getLogger(__name__)


@job
def price_update():
    response = requests.get("https://www.nbrb.by/api/exrates/rates?periodicity=0")
    result = response.json()
    item = "Empty"
    for item in result:
        if item["Cur_Abbreviation"] == "USD":
            break
    query = Product.objects.update(price_usd=F("price") / Decimal(item["Cur_OfficialRate"]))
    # for product in get_products:
    #     product.price_usd = float(product.price) / item["Cur_OfficialRate"]
    #     product.save()



class Command(BaseCommand):
    help = "Crawl OMA catalog"

    def handle(self, *args, **options):
        price_update()


