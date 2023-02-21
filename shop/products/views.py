from django.shortcuts import render

# Create your views here.
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info(request.GET, request.POST)
    if request.GET.get("key") is not None:
        logger.info(request.GET.get("key"))
        return HttpResponse(f"Your GET query is 'key = {request.GET.get('key')}'")
    return HttpResponse("Shop index view")


def profile(request):
    logger.info(request.GET, request.POST)
    return HttpResponse("Profile page")