from .topology_map import *
from .topology_graph import *
import pprint
import sys
from .topology_recursionlimit import *
import time

tm = TopologyMapper()
tg = TopologyGraph()
from singleton import Singleton
config = Singleton
# dict_rt, int_ip_rt, int_sp_rt = tm.getRouterTopology()
# dict_sw, int_ip_sw, int_sp_sw = tm.getSwitchTopology()

dict_tp = config.path_graph
pprint.pprint(dict_tp)

start = '127.8.8.1'
end = '192.168.1.3'
with RecursionLimit(3000):
    path = tg.find_path(dict_tp, start, end,None,'192.168.1.1')
    print(path)
path = tg.RemoveRedundentRouterIPs(config.routers_interfaces, path)
print(path)
