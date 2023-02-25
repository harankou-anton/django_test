import os

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

    if int(os.getenv(key='FIRST_ENV_PARAM')) % 2 != 0:
        logger.info(f'first environment variable is {os.getenv(key="SECOND_ENV_PARAM")}')
    else:
        logger.info(f'first environment variable is {os.getenv(key="THIRD_ENV_PARAM")}')
    return HttpResponse("Shop index view")

