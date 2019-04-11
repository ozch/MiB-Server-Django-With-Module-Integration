"""
WSGI config for MIBServer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
import os
import subprocess
import time
import pprint
from background_task.models_completed import CompletedTask
from background_task.models import Task
from BackgroundJobs import tasks
from BackgroundJobs.models import *
from singleton import Singleton
from logging import getLogger

logger = getLogger(__name__)
config = Singleton

print(">> Initializing Packet Flow Collector Module...")
try:
    pc_command = "python " + os.path.dirname(__file__) + "\\PacketFlowCollector\\packetflow_collector.py"
    #subprocess.Popen(pc_command,close_fds=True)
except:
    print(
        ">> Error : Port Error Occured While Initializng Packet Flow Collector \n Try Force Closing Port : {} and Restating The Server...".format(
            config.pktflw_port))

print(">> Initializing Network Topology Mapping...")
tasks.TopologyMappingInit()
print("Network Topology:")
pprint.pprint(config.topology)
print("Network Graph:")
pprint.pprint(config.path_graph)
print("Devices List:")
pprint.pprint(config.network_devices)
print("Servers List:")
pprint.pprint(config.server_list)
time.sleep(1)
# Todo : this need to be change according to number of device in network
print(">> Deleting Previouslly Uncompleted Jobs...")
Task.objects.all().delete()
print(">> Clearing Previous Port Scan Data...")
Task.objects.all().delete()
print(">> Dumping Previous Flow Data...")
from django.core import serializers
from PacketFlow.models import Netflow
#DumpData = Netflow.objects.all()
#data = serializers.serialize("json",DumpData)
#timestr ='FlowDumps/'+time.strftime("%Y%m%d-%H%M%S")+'.json'
#out = open(timestr, "w")
#out.write(data)
#out.close()
#DumpData.delete()
#time.sleep(2)
print(">> Initializing  New Jobs...")
print(">> Initializing Open Port Scanner...")
#tasks.PortScanningThread(repeat=config.port_scan_scan_intervel,repeat_until=None)
print(">> Initializing Packet Sniffer Scanner...")
tasks.TopologyMapping(repeat=config.topology_scan_intervel,repeat_until=None)

print(">> Operation Completed...\n Status:Running...")
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MIBServer.settings')
application = get_wsgi_application()
