# Create your views here.
import logging
from django.core.paginator import Paginator
from django.db.models import Sum, F
from products.models import Product
from django.shortcuts import render, redirect
from products.forms import ProductAdd

logger = logging.getLogger(__name__)


def index(request):
    # result = cache.get("products-view")
    # if result is not None:
    #     return result
    get_all_products = Product.objects.all()

    if request.GET.get("title"):
        get_all_products = get_all_products.get(title=request.GET.get("title"))
        consumers = get_all_products.purchases.all().distinct("user_id")
        return render(
            request,
            "product_details.html",
            {"get_all_products": get_all_products, "consumers": consumers},
        )
    if request.GET.get("color"):
        get_all_products = get_all_products.filter(
            color__icontains=request.GET.get("color")
        )

    if request.GET.get("sort") == "price":
        get_all_products = get_all_products.order_by("-price")

    if request.GET.get("sort") == "popularity":
        get_all_products = get_all_products.annotate(
            count_sum=Sum("purchases__count")
        ).order_by("-count_sum")

    if request.GET.get("sort") == "purchased_money":
        get_all_products = get_all_products.annotate(
            purchased_money=Sum(F("price") * F("purchases__count"))
        ).order_by("-purchased_money")
    paginator = Paginator(get_all_products, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # response = render(request, 'index.html', {'page_obj': page_obj})
    # cache.set("products-view", response, 60 * 60)
    return render(request, "index.html", {"page_obj": page_obj})
    # return response


def add_product(request):
    form = ProductAdd()
    if request.method == "POST":
        form = ProductAdd(request.POST)
        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data["title"],
                price=form.cleaned_data["price"],
                description=form.cleaned_data["description"],
                color=form.cleaned_data["color"],
            )
            return redirect("index")
    else:
        form = ProductAdd()

    return render(request, "product_add.html", {"form": form})
