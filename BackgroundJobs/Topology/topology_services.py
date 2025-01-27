from singleton import Singleton
from .topology_graph import TopologyGraph
from Topology.models import TopologyServer
from .topology import Topology
import time
from .mysql_connection import *


def NetworkTopologyScanThread():
    config = Singleton
    tp = Topology()
    tg = TopologyGraph()
    print(">>Starting Job: Scanning Network...")
    while True:
        if config.mutex == 0:
            config.mutex = 1
            # getting topology from devices
            dict_tp = tp.getTopology()
            graph_path, all_devices_list = tg.GenerateGraph(dict_tp)
            config.all_devices_list = all_devices_list
            router_interfaces = tg.GetRouterInterfaceIP(dict_tp)
            # saving to singleton class
            config.topology = dict_tp
            config.path_graph = graph_path
            config.routers_interfaces = router_interfaces
            config.network_devices = GetNetworkDevies(graph_path, router_interfaces)
            config.mutex = 0
            break
        else:
            time.sleep(5)
    print(">>Ending Job: Scanning Network...")

def GetServerIPList():
    list = []
    servers = TopologyServer.objects.all()
    for server in servers:
        list.append(server.ip)
    return list
def GetNetworkDevies(path_graph, router_interfaces):
    network_list = []
    for key in path_graph:
        network_list.append(key)
    con = MySQLConnection().initConnection()
    cursor = con.cursor()
    cursor.execute("SELECT hostname FROM topology_ssh")
    removeable_ip = cursor.fetchall()
    for removeable in removeable_ip:
        if removeable[0] in network_list:
            network_list.remove(removeable[0])
    router_ip_list = GetRouterInterfaceIPList(router_interfaces)
    for ip in router_ip_list:
        if ip in network_list:
            network_list.remove(ip)
    return network_list


def GetRouterInterfaceIPList(router_interfaces):
    router_ip_list = []
    for key in router_interfaces:
        for ip in router_interfaces[key]:
            router_ip_list.append(ip)
    return router_ip_list


if __name__ == '__main__':
    NetworkTopologyScanThread()
