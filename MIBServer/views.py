from django.shortcuts import render
from AgentControl.models import *
from singleton import Singleton
from django.utils import timezone
config = Singleton
def Dashboard(request):
    routers,switches,devices = CountDevices(config.all_devices_list)
    agents = DeviceInfo.objects.all().count()
    now = timezone.now()
    reference_time = now - timezone.timedelta(seconds=6)
    print(reference_time)
    online_agents = Execute.objects.filter(online__gte=reference_time).count()
    context = {
        'page_title' : "- Dashboard",
        'routers': routers,
        'switches':switches,
        'devices':devices,
        'agents':agents,
        'activeagents':online_agents
    }
    return render(request=request,template_name='dashboard.html',context=context)

def CountDevices(list):
    routers,switches,servers,devices = 0,0,0,0
    for instance_ in list:
        if instance_['type'].lower() == 'device' or instance_['type'].lower() == 'server' :
            devices = devices + 1
        elif instance_['type'].lower() == 'switch':
            switches = switches + 1
        elif instance_['type'].lower() == 'router':
            routers = routers + 1
    return routers,switches,devices