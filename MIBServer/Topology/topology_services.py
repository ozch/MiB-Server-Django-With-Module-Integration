from singleton import  Singleton
from .topology_graph import TopologyGraph
from .topology import Topology
import time

def NetworkTopologyScanThread():
    config = Singleton
    tp = Topology()
    tg = TopologyGraph()
    while True:
        if str(config.mutex) == 0:
            config.mutex = 1
            #getting topology from devices
            dict_tp = tp.getTopology()
            graph_path = tg.GenerateGraph(dict_tp)
            router_interfaces = tg.GetRouterInterfaceIP(dict_tp)
            #saving to singleton class
            config.topology = dict_tp
            config.path_graph = graph_path
            config.routers_interfaces = router_interfaces
            config.mutex = 0
            break
        else:
            time.sleep(5)

# import threading
# class ThreadRipper(threading.Thread):
#     def __init__(self, function):
#         threading.Thread.__init__(self)
#         self.runnable = function
#     def run(self):
#         self.runnable()


