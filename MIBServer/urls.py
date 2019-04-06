"""MIBServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from AgentControl import views as agent_views
from Topology import views as topology_views
from PacketFlow import views as packet_views
from BackgroundJobs import views as job_views
from . import views as main_view

admin.site.site_header = "NetworkEngine Administration"
admin.site.site_title = "AdminPanel - NetworkEngine"
admin.site.index_title = "Logout of the system before leaving.."
urlpatterns = [
    path('admin/', admin.site.urls),
    #From MIBServer
    path('',main_view.LogIn, name="login_page"),
    path('login',main_view.LogInAction, name="login"),
    path('index/',  main_view.Dashboard,name='index'),
    #From AgentControl App
    path('token_gen/',agent_views.TokenGeneration,name='token_gen'),
    path('token_active/',agent_views.TokenActive,name='token_active'),
    path('agents/',agent_views.Agents,name='agents'),
    path('agent/<str:mac>/',agent_views.AgentDetails,name='agent_details'),
    path('agent/<str:mac>/<str:pn>/endtask',agent_views.ProcessKill,name='process_kill'),
    path('agent/<str:mac>/<str:action>/boot',agent_views.BootControl,name='boot_control'),
    path('agent/<str:mac>/<str:srv>/<str:op>',agent_views.ServiceControl,name='service_control'),
    path('agent/<str:mac>/execute',agent_views.Execute,name='execute'),
    path('uuid_gen/', agent_views.GenerateTokenAction, name='uuid_gen'),
    #From BackgroundJobs
    path('openports/',job_views.OpenPortScan,name='openports'),
    path('snifferscan/',job_views.SnifferScan,name='snifferscan'),
    #From Topology App
    path('network_devices/',topology_views.NetworkDevices,name='network_devices'),
    #From PacketFlow App
    path('visualization/',packet_views.Visualization,name='visualization'),
    path('packetflow/', packet_views.PacketFlow, name='packetflow')



    #APIs
    #To be written

]
