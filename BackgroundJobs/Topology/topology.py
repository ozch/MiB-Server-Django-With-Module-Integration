from .topology_map import TopologyMapper
from .topology_collector import TopologyCollector


# Todo: Join switch and router  interfaces and speed list get in return from TopologyMapper()
class Topology():
    def __init__(self):
        self.tm = TopologyMapper()
        self.tc = TopologyCollector()

    def getTopology(self):
        self.tc.collectRawNetwokData()
        dict = self.tm.getTopology()
        return dict
