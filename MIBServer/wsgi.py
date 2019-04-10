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

from logging import getLogger

logger = getLogger(__name__)
config = Singleton

logger.info(">> Initializing Packet Flow Collector Module...")
try:
    pc_command = "python " + os.path.dirname(__file__) + "\\PacketFlowCollector\\packetflow_collector.py"
    subprocess.Popen(pc_command,close_fds=True)
except:
    logger.info(
        ">> Error : Port Error Occured While Initializng Packet Flow Collector \n Try Force Closing Port : {} and Restating The Server...".format(
            config.pktflw_port))

logger.info(">> Initializing Network Topology Mapping...")
tasks.TopologyMappingInit()
# tasks.PortScanningThreadInit()
# Todo : this need to be change according to number of device in network
logger.info(">> Deleting Previouslly Uncompleted Jobs...")
from background_task.models import Task
Task.objects.all().delete()
time.sleep(10)
logger.info(">> Initializing  New Jobs...")
logger.info(">> Initializing Open Port Scanner...")
tasks.PortScanningThread(repeat=config.port_scan_scan_intervel,repeat_until=None)
logger.info(">> Initializing Packet Sniffer Scanner...")
tasks.TopologyMapping(repeat=config.topology_scan_intervel,repeat_until=None)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MIBServer.settings')
application = get_wsgi_application()
