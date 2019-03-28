"""
WSGI config for MIBServer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
import os
import pprint
from .Topology import topology_services
from singleton import Singleton
import subprocess
from django.core.wsgi import get_wsgi_application
from MIBServer.PacketFlowCollector import packetflow_collector
command = "python "+os.path.dirname(__file__)+"\PacketFlowCollector\packetflow_collector.py"
print(command)
#subprocess.Popen(command,close_fds=True)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MIBServer.settings')
application = get_wsgi_application()

# config = Singleton
# topology_services.NetworkTopologyScanThread()
# pprint.pprint(config.routers_interfaces)
# pprint.pprint(config.path_graph)
# pprint.pprint(config.topology)