
# Create your views here.
import logging
from django.db.models import Sum, F
from django.http import HttpResponse
from django.conf import settings
from products.models import Product
from django.shortcuts import render, redirect
from products.forms import ProductAdd
logger = logging.getLogger(__name__)


def index(request):
    get_all_products = Product.objects.all()
    if request.GET.get("title"):
        get_all_products = get_all_products.filter(title=request.GET.get("title"))

    if request.GET.get("color"):
        get_all_products = get_all_products.filter(color__icontains=request.GET.get("color"))

    if request.GET.get("sort") == 'price':
        get_all_products = get_all_products.order_by('-price')

    if request.GET.get("sort") == 'popularity':
        get_all_products = get_all_products.annotate(count_sum=Sum("purchases__count")).order_by('-count_sum')

    if request.GET.get("sort") == 'purchased_money':
        get_all_products = get_all_products.annotate(
            purchased_money=Sum(F('price')*F('purchases__count'))).order_by('-purchased_money')

    return render(request, 'index.html', {"get_all_products": get_all_products})


def add_product(request):
    form = ProductAdd()
    if request.method == "POST":
        form = ProductAdd(request.POST)
        if form.is_valid():
            Product.objects.create(title=form.cleaned_data["title"],
                                   price=form.cleaned_data["price"],
                                   description=form.cleaned_data["description"],
                                   color=form.cleaned_data["color"])
            return redirect("index")
    else:
        form = ProductAdd()

    return render(request, "product_add.html", {"form": form})
