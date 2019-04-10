from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
import uuid
from django.core.exceptions import ObjectDoesNotExist

from django.urls import reverse
from BackgroundJobs.models import *
import time
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
        'offline': offline_agents
    }
    return render(request=request, template_name='agents.html', context=context)


def AgentDetails(request, mac, tab):
    sysinfo = DeviceInfo.objects.get(mac_address=mac)
    processes = ProcessInfo.objects.get(mac_address=mac)
    services = ServicesInfo.objects.get(mac_address=mac)
    openports = NetworkPortScanner.objects.filter(ip=sysinfo.ip_address)
    context = {
        'page_title': "- Agent Details",
        'sysinfo': sysinfo.sys_info,
        'processes': processes.process_info,
        'services': services.services_info,
        'openports': openports,
        'device_mac': mac,
        'tabv': tab
    }
    return render(request=request, template_name='agent_detail.html', context=context)


def TokenGeneration(request):
    unusedtokens = TokenStore.objects.filter(is_taken=0)
    context = {
        'page_title': "- Token Generation",
        'unusedtokens': unusedtokens
    }
    return render(request=request, template_name='token_gen.html', context=context)


def GenerateTokenAction(request):
    str = uuid.uuid4()
    instance = TokenStore(is_taken=0, token=str.__str__())
    instance.save()
    return redirect(reverse(TokenGeneration))


def TokenActive(request):
    activetokens = Token.objects.all()

    context = {
        'page_title': "- Active Tokens",
        'activetokens': activetokens
    }
    return render(request=request, template_name='token_active.html', context=context)


def Execution(request, mac, is_first):
    data = request.POST
    if is_first.lower() == 'true':
        scrpt = Execute.objects.get(mac_address=mac)
        scrpt.script_flag = 1
        scrpt.script = data.get('script')
        scrpt.save()
        print(scrpt)

        scrpt = Execute.objects.get(mac_address=mac)
        context = {
            'script': scrpt.script,
            'mac': scrpt.mac_address,
            'is_first': 'false',
            'tab': 'E'
        }
        time.sleep(5)
        return render(request=request, template_name='script.html', context=context)
    else:
        time.sleep(5)
        scrpt = Execute.objects.get(mac_address=mac)
        context = {
            'script': scrpt.script,
            'mac': scrpt.mac_address,
            'is_first': 'false',
            'tab': 'E'
        }
        return render(request=request, template_name='script.html', context=context)


def ProcessKill(request, mac, pn):
    kill = Execute.objects.get(mac_address=mac)
    kill.kill_flag = 1
    kill.kill_name = pn + '.exe'
    kill.save()
    time.sleep(5)
    return redirect(reverse('agent_details', kwargs={'mac': mac, 'tab': 'P'}))


def BootControl(request, mac, action):
    cntrl = Execute.objects.get(mac_address=mac)
    cntrl.boot_flag = 1
    cntrl.boot_command = action
    cntrl.save()
    time.sleep(5)
    return redirect(reverse(Agents))


def ServiceControl(request, mac, srv, op):
    srv_cntrl = Execute.objects.get(mac_address=mac)
    srv_cntrl.service_flag = 1
    srv_cntrl.service_name = op + ";" + srv
    srv_cntrl.save()
    time.sleep(5)
    return redirect(reverse('agent_details', kwargs={'mac': mac, 'tab': 'S'}))


def TokenAuthentication(request, mac, token):
    try:
        token_exist = TokenStore.objects.get(token=token)
    except ObjectDoesNotExist:
        return HttpResponse("401")
    if int(token_exist.is_taken) == 1:
        try:
            token_auth_check = Token.objects.get(token=token, mac=mac)
            return HttpResponse("200")
        except ObjectDoesNotExist:
            return HttpResponse("401")
    if int(token_exist.is_taken) == 0:
        token_exist.is_taken = 1
        token_exist.save()
        token_set = Token(token=token, mac=mac)
        token_set.save()
        return HttpResponse("200")
