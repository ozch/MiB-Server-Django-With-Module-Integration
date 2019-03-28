import yaml

class Singleton():
    __instance = None
    f = open('config.yaml', 'r')

    #mutex lock for threads
    mutex = 0

    config = yaml.safe_load(f)
    #Module Intercommunication variables
    flow_id = 0
    path_graph = {}
    routers_interfaces = {}
    topology = {}
    interfaces_list = {}

    #Configuration variables

    #Database Configurations
    db_host = config["database"]["host"]
    db_port = config["database"]["port"]
    db_username = config["database"]["username"]
    db_password = config["database"]["password"]
    db_schema = config["database"]["schema"]

    #Topology Configurations
    topology_scan_intervel = config["topology"]["scan_intervel"]

    #PortScan Configurations
    port_scan_alpha = config["portscan"]["alpha"]
    port_scan_omega = config["portscan"]["omega"]
    port_scan_scan_intervel = config["portscan"]["scan_intervel"]

    # SnifferScan Configurations
    sniffer_scan_alpha = config["portscan"]["alpha"]
    sniffer_scan_omega = config["portscan"]["omega"]
    sniffer_scan_scan_intervel = config["portscan"]["scan_intervel"]

    #PacketFlow Configurations
    pktflw_host_ip = config["packetflow"]["host_ip"]
    pktflw_port = config["packetflow"]["port"]








    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self
