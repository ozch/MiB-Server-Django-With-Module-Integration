"""
WSGI config for MIBServer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

# from .module_integration import start_services
# from .module_integration.topology_graph import TopologyGraph
# import pprint
# from singleton import Singleton
# import threading
import os

# print("Starting module...")
# print("Starting PacketFlow Collector...")
# pkt_thread = threading.Thread(target=start_services.PacketFlowCollectorThread(),args=())
# pkt_thread.setDaemon(True)
# pkt_thread.start()
# print("Starting Topology Mapper and Raw Data Collector Collector...")
# nws_thread = threading.Thread(target=start_services.NetworkTopologyScanThread(),args=())
# nws_thread.setDaemon(True)
# nws_thread.start()
# print(">>><<<>>><<<>>><<<>>><<<>>><<<>>><<<>>>")
# tg = TopologyGraph()
# config = Singleton
# pprint(config.topology)
# pprint(config.path_graph)
# start = '192.168.2.1'
# end = '192.168.0.3'
# path = tg.find_path(config.path_graph,start, end)
# print(path)
# path=tg.RemoveRedundentRouterIPs(config.routers_interfaces,path)
# print(path)
# print(">>><<<>>><<<>>><<<>>><<<>>><<<>>><<<>>>")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MIBServer.settings')

application = get_wsgi_application()
