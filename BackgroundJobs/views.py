from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from logging import getLogger

from .tasks import demo_job
from background_task import background
logger = getLogger(__name__)

@background(schedule=10)
def tasks():
    logger.log("Task Done...")
    print("Task Done")
