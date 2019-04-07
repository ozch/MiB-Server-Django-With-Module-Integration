"""
WSGI config for MIBServer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
import os
import subprocess
import time
from BackgroundJobs.Topology.mysql_connection import *
from BackgroundJobs import tasks
from singleton import Singleton

con = MySQLConnection().initConnection()
cursor = con.cursor()
cursor.execute("SELECT max(id) FROM netflow_v")
flow_pk = cursor.fetchone()
config = Singleton
config.flow_id = flow_pk[0]

cursor.close()
con.close()

print(">> Initializing Packet Flow Collector Module...")
try:
    pc_command = "python " + os.path.dirname(__file__) + "\\PacketFlowCollector\\packetflow_collector.py"
#    subprocess.Popen(pc_command,close_fds=True)
except:
    print(
        ">> Error : Port Error Occured While Initializng Packet Flow Collector \n Try Force Closing Port : {} and Restating The Server...".format(
            config.pktflw_port))

print(">> Initializing Network Topology Mapping...")
tasks.TopologyMappingInit()
print(config.topology)
# tasks.PortScanningThreadInit()
# Todo : this need to be change according to number of device in network
print(">> Deleting Previouslly Uncompleted Jobs...")
from background_task.models import Task

Task.objects.all().delete()
# time.sleep(10)
print(">> Initializing  New Jobs...")
print(">> Initializing Open Port Scanner...")
# tasks.PortScanningThread(repeat=config.port_scan_scan_intervel,repeat_until=None)
print(">> Initializing Packet Sniffer Scanner...")
# tasks.TopologyMapping(repeat=config.topology_scan_intervel,repeat_until=None)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MIBServer.settings')
application = get_wsgi_application()
