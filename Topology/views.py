from django.shortcuts import render
from singleton import Singleton
def NetworkDevices(request):
    config = Singleton
    context = {
        'page_title': "- Network Devices",
        'devices_list': config.all_devices_list,
        'topology_data': config.topology
    }
    return render(request=request,template_name='network_devices.html',context=context)
