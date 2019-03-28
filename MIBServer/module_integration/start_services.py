from singleton import  Singleton
from .topology_graph import TopologyGraph
from .topology import Topology
from .topology_recursionlimit import RecursionLimit
from MIBServer.module_integration import packetflow_collector
import time
def NetworkTopologyScanThread():
    config = Singleton
    tp = Topology()
    tg = TopologyGraph()
    while(True):
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
            time.sleep(config.topology_scan_intervel)
        else:
            time.sleep(5)
from MIBServer.module_integration import packetflow_collector
def PacketFlowCollectorThread():
    packetflow_collector.initFlowCollector()

import threading
class ThreadRipper(threading.Thread):
    def __init__(self, function):
        threading.Thread.__init__(self)
        self.runnable = function
    def run(self):
        self.runnable()


