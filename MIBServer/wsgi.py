"""
WSGI config for MIBServer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
import os
import subprocess
import time

from BackgroundJobs import tasks
from singleton import Singleton

pc_command = "python "+os.path.dirname(__file__)+"\\PacketFlowCollector\\packetflow_collector.py"
print(pc_command)
subprocess.Popen(pc_command,close_fds=True)

config = Singleton
tasks.TopologyMappingInit()
#Todo : this need to be change according to number of device in network
time.sleep(10)
from background_task.models import Task
Task.objects.all().delete()
tasks.PortScanningThread(repeat=config.port_scan_scan_intervel,repeat_until=None)
tasks.TopologyMapping(repeat=config.topology_scan_intervel,repeat_until=None)


from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MIBServer.settings')
application = get_wsgi_application()

