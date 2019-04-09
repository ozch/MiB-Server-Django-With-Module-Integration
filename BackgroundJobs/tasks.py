from background_task import background
from .Topology import topology_services as tp
from .NetworkScanning import port_scanner as ps

from singleton import Singleton

config = Singleton


@background(schedule=config.topology_scan_intervel)
def TopologyMapping():
    tp.NetworkTopologyScanThread()


def TopologyMappingInit():
    tp.NetworkTopologyScanThread()


@background(schedule=config.port_scan_scan_intervel)
def PortScanningThread():
    ps.PortScanner()


def PortScanningThreadInit():
    ps.PortScanner()
