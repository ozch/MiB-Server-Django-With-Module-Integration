import yaml
class Singleton():
    __instance = None
    f = open('config.yaml', 'r')
    config = yaml.safe_load(f)
    # Module Intercommunication variables

    # Database Configurations
    db_host = config["database"]["host"]
    db_port = config["database"]["port"]
    db_username = config["database"]["username"]
    db_password = config["database"]["password"]
    db_schema = config["database"]["schema"]

    # PacketFlow Configurations
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
