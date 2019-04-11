import yaml


class Singleton():
    __instance = None
    f = open('config.yaml', 'r')
    # mutex lock for threads/async functions
    mutex = 0

    config = yaml.safe_load(f)
    # Module Intercommunication variables
    flow_id = 0 #Currently Not Being Used
    path_graph = {}
    routers_interfaces = {}
    topology = {}
    interfaces_list = {}
    # network devices contain only server and devices
    network_devices = {}
    # all devices contain everything including switches and routers
    all_devices_list = []
    # all server ip list
    server_list = []
    # Configuration variables

    # Database Configurations
    db_host = config["database"]["host"]
    db_port = config["database"]["port"]
    db_username = config["database"]["username"]
    db_password = config["database"]["password"]
    db_schema = config["database"]["schema"]

    # Topology Configurations
    topology_scan_intervel = config["topology"]["scan_intervel"]

    # PortScan Configurations
    port_scan_scan_intervel = config["portscan"]["scan_intervel"]

    # PacketFlow Configurations
    pktflw_host_ip = config["packetflow"]["host_ip"]
    pktflw_port = config["packetflow"]["port"]

    pktflw_vis_intervel = config["packetvis"]["intervel"]
    pktflw_vis_pkt_eql = config["packetvis"]["packet_eql"]

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This is a singleton class! \n It is being used for data sharing only.")
        else:
            Singleton.__instance = self
