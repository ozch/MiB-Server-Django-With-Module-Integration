from django.shortcuts import render

def Visualization(request):
    context = {
        'page_title': "- Visualization"
    }
    return render(request=request,template_name='network_devices.html',context=context)
def PacketFlow(request):
    context = {
        'page_title': "- PacketFlow"
    }
    return render(request=request,template_name='network_devices.html',context=context)
# Create your views here.
