"""
WSGI config for MIBServer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
import os
import pprint
from singleton import Singleton
import asyncio
import threading
import subprocess
from multiprocessing import Process
from .Topology import topology_services as ts
from .NetworkScanning import port_scanner as ps
#
# thread_tp = threading.Thread(target=ts.NetworkTopologyScanThread())
# thread_tp.start()
# print("Thread Running Going to Sleep")

pc_command = "python "+os.path.dirname(__file__)+"\\PacketFlowCollector\\packetflow_collector.py"
print(pc_command)
subprocess.Popen(pc_command,close_fds=True)
from BackgroundJobs import tasks
tasks.demo_job()

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MIBServer.settings')
application = get_wsgi_application()

