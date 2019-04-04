from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from logging import getLogger
from .models import *
from background_task import background

def OpenPortScan(request):
    openports = NetworkPortScanner.objects.all()
    context = {
        'page_title': "- Open Port Scanner",
        'openports':openports
    }
    return render(request=request,template_name='portscan.html',context=context)
def SnifferScan(request):
    sniffers = NetworkSnifferScanner.objects.filter(is_sniffer=1)
    context = {
        'page_title': "- Packet Sniffer Scanner",
        'sniffers':sniffers
    }
    return render(request=request,template_name='snifferscan.html',context=context)