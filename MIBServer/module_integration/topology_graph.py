import sys

class TopologyGraph():
    def __init__(self):
        self.graph_tp = {}
    #creates graph from topology dict obtained from topology_map.getTopology()
    def GenerateGraph(self,dict_tp):
        self.graph_tp = {}
        self.GraphRouterPoints(dict_tp)

        return self.graph_tp

    def AjacentChildPathMapping(self,graph_node,node_childs,parent_ip):
        for child in node_childs:
            graph_node.append(child["ip"])
            if "child" in child:
                if isinstance(parent_ip,list):
                    self.graph_tp[child["ip"]] = []
                    for interface in parent_ip:
                        self.graph_tp[child["ip"]].append(interface)
                else:
                    self.graph_tp[child["ip"]] = [parent_ip]
                self.AjacentChildPathMapping(self.graph_tp[child["ip"]],child["child"],child["ip"])
            else:
                if isinstance(parent_ip,list):
                    self.graph_tp[child["ip"]] = []
                    for interface in parent_ip:
                        self.graph_tp[child["ip"]].append(interface)
                else:
                    self.graph_tp[child["ip"]] = [parent_ip]
    def GraphRouterPoints(self,dict_tp):
        for key in dict_tp:
            if dict_tp[key]["type"].lower() == "router":
                for c in dict_tp[key]["ip"]:
                    self.graph_tp[c] = []
                    self.addRouterInterfaceIP(self.graph_tp[c],c,dict_tp[key])
                    self.AjacentChildPathMapping(self.graph_tp[c],dict_tp[key]["child"],dict_tp[key]["ip"])
    def addRouterInterfaceIP(self,path_start_node,path_start_ip,router):
        for ip in router["ip"]:
            if ip == path_start_ip:
                continue
            else:
                path_start_node.append(ip)

    def find_path(self,graph, start_vertex, end_vertex, path=None):
        if path == None:
            path = []
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(graph,vertex, end_vertex, path)
                if extended_path:
                    return extended_path
        return None

    def GetRouterInterfaceIP(self, dict_tp):
        graph = {}
        for key in dict_tp:
            graph[key] = dict_tp[key]["ip"]
        return graph
    def RemoveRedundentRouterIPs(self,routers,path):
        len(path)
        list_remove = []
        for key in routers:
            prev = path[0]
            for i in range(1,len(path)):
                now = path[i]
                if prev in routers[key] and now in routers[key]:
                    list_remove.append(now)
                prev = now
        for item in list_remove:
            path.remove(item)
        return path


