from .topology_map import *
from .topology_graph import *
import pprint
import sys
from .topology_recursionlimit import *
import time
tm = TopologyMapper()
tg = TopologyGraph()
from singleton import Singleton
# dict_rt, int_ip_rt, int_sp_rt = tm.getRouterTopology()
# dict_sw, int_ip_sw, int_sp_sw = tm.getSwitchTopology()
dict_tp = tm.getTopology()
pprint.pprint(dict_tp)
dict_tp= {
    "1": {
        "type": "router",
        "mac": "BA03ADEAE2A0",
        "speed": "1000",
        "ip": ["192.168.1.1", "192.168.2.1", "192.168.3.1","192.168.0.1"],
        "child": [
            {
                "type": "server",
                "mac": "EBA6D7E41A34",
                "speed": "1000",
                "ip": "192.168.1.10",
            },
            {
                "type": "device",
                "mac": "EBA6D7E41A34",
                "speed": "1000",
                "ip": "192.168.1.11",
            },
            {
                "type": "switch",
                "mac": "EBA6D7E41A34",
                "speed": "1000",
                "ip": "192.168.0.2",
                "child":
                    [
                        {
                            "type": "device",
                            "mac": "EBA6D7E41A35",
                            "speed": "60",
                            "ip": "192.168.0.3"
                        }
                    ]
            },
            {
                "type": "switch",
                "mac": "EBA6D7E41A34",
                "speed": "1000",
                "ip": "192.168.1.2",
                "child":
                    [
                        {
                            "type": "device",
                            "mac": "EBA6D7E41A35",
                            "speed": "60",
                            "ip": "192.168.1.3"
                        },
                        {
                            "type": "device",
                            "mac": "EBA6D7E41A6",
                            "speed": "60",
                            "ip": "192.168.1.4"
                        },
                        {
                            "type": "switch",
                            "mac": "484AD7233FE7",
                            "speed": "1000",
                            "ip": "192.168.2.2",
                            "child":
                                [
                                    {
                                        "type": "device",
                                        "mac": "DBA6D7E41A35",
                                        "speed": "60",
                                        "ip": "192.168.2.3"
                                    },
                                    {
                                        "type": "device",
                                        "mac": "DBA6D7E41A6",
                                        "speed": "60",
                                        "ip": "192.168.2.4"
                                    }
                                ]
                        }
                    ]
            }

        ]
    }
}
pprint.pprint(dict_tp)
graph = tg.GenerateGraph(dict_tp)
pprint.pprint(graph)
router_interfaces = tg.GetRouterInterfaceIP(dict_tp)
start = '192.168.2.1'
end = '192.168.0.3'
with RecursionLimit(3000):
    path = tg.find_path(graph,start, end)
    print(path)
path=tg.RemoveRedundentRouterIPs(router_interfaces,path)
print(path)

