from django.shortcuts import render
from django.utils import timezone

from .models import *
def Agents(request):
    print(timezone.get_current_timezone())
    now = timezone.now()
    reference_time = now - timezone.timedelta(seconds=6)
    print(reference_time)
    online_agents = Execute.objects.filter(online__gte=reference_time)
    online_list = []
    for online in online_agents:
        online_list.append(online.mac_address)

    online_agents = DeviceInfo.objects.filter(mac_address__in=online_list)
    offline_agents = DeviceInfo.objects.all().exclude(mac_address__in=online_list)
    context = {
        'page_title': "- Agents",
        'online': online_agents,
        'offline':offline_agents
    }
    return render(request=request,template_name='agents.html',context=context)

def AgentDetails(request):
    context = {
        'page_title': "- Agent Details"
    }
    return render(request=request,template_name='agent_detail.html',context=context)

def TokenGeneration(request):
    unusedtokens = TokenStore.objects.filter(is_taken=0)
    context = {
        'page_title': "- Token Generation",
        'unusedtokens': unusedtokens

    }
    context = {
        'page_title': "- Token Generation"
    }
    return render(request=request,template_name='token_gen.html',context=context)
import uuid
def GenerateTokenAction(request):
    str = uuid.uuid4()
    instance = TokenStore(is_taken=0,token=str.__str__())
    instance.save()
    unusedtokens = TokenStore.objects.filter(is_taken=0)
    context = {
        'page_title': "- Token Generation",
        'unusedtokens': unusedtokens

    }
    return render(request=request,template_name='token_gen.html',context=context)

def TokenActive(request):
    activetokens = Token.objects.all()

    context = {
        'page_title': "- Active Tokens",
        'activetokens':activetokens
    }
    return render(request=request,template_name='token_active.html',context=context)


def Execution(request):
    context = {
        'page_title': "- Execution Window"
    }
    return render(request=request,template_name='404.html',context=context)

