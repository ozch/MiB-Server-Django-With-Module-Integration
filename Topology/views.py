from django.shortcuts import render
def NetworkDevices(request):
    context = {
        'page_title': "- Network Devices"
    }
    return render(request=request,template_name='network_devices.html',context=context)
