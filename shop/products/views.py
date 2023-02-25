from django.shortcuts import render

# Create your views here.
import logging
from django.http import HttpResponse
from django.conf import settings

logger = logging.getLogger(__name__)


def index(request):
    if request.GET.get("param"):
        logger.info(f'Custom var = {settings.MY_CUSTOM_VARAIBLE}')
        logger.info(f'Custom env var = {settings.MY_ENV_VARAIBLE}')
        logger.info(f"My param = {request.GET.get('param')}")
    return HttpResponse("Shop index view")

