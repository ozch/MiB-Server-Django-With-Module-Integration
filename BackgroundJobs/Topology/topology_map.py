from .mysql_connection import MySQLConnection
import ipaddress

from difflib import SequenceMatcher
import pprint

class TopologyMapper():

    def __init__(self):
        self.con = MySQLConnection().initConnection()
        self.cursor = self.con.cursor()

    def areInSameNetwork(self, parent_ip, child_ip, parent_host_bit):
        parent = str(parent_ip) + '/' + str(parent_host_bit)
        child = str(child_ip) + '/' + str(parent_host_bit)
        parent_network = ipaddress.ip_network(parent, False)
        child_network = ipaddress.ip_network(child, False)
        if child_network == parent_network:
            return True
        else:
            return False

    def isNotASwithcIP(self, ip, switchs):
        for switch in switchs:
            if switch[0] == ip:
                return False
        return True

    # Returns interface speed of interface for routers
    def getInterfaceSpeedIntRouter(self, str_int):
        rat = SequenceMatcher(None, "GigabitEthernet", str_int).ratio()
        if rat > 0.75:
            return 1000
        else:
            rat = SequenceMatcher(None, "FastEthernet", str_int).ratio()
            if rat > 0.75:
                return 100
            else:
                return 60

    def isMacBridgeExist(self, mac_a, mac_b):
        rat = SequenceMatcher(None, mac_a, mac_b).ratio()
        if rat > 0.75:
            return True
        else:
            return False

    # Returns interface speed of interface for switches
    def getInterfaceSpeedIntSwitch(self, str_int):
        if str_int.startswith("g") or str_int.startswith("G"):
            return 1000
        else:
            if str_int.startswith("F") or str_int.startswith("f"):
                return 100
            else:
                return 60

    # This Function is Used to add switch to switch bridges between remaining switches
    def addSwitchSwitchBridges(self, dict_rt, dict_sw):
        # print("Adding switch to switch bridges...")
        list_remove_switches = []
        self.cursor.execute("SELECT ip,bridge FROM mib.topology_bridge")
        bridges = self.cursor.fetchall()
        ip_list = self.getSwitchIPs(dict_sw)
        for bridge in bridges:
            if bridge[0] not in ip_list:
                continue
            for key in dict_sw:
                # possible_con(parent_ip,mac,type,port)
                self.cursor.execute("SELECT host_bits FROM mib.topology_ssh where hostname='{}'".format(bridge[0]))
                host_bits = self.cursor.fetchone()
                # print(host_bits)
                if self.areInSameNetwork(bridge[0], dict_sw[key]["ip"], host_bits[0]):
                    self.cursor.execute(
                        "select * from (select parent_ip,mac,type,port from mib.topology_hardware where parent_ip!='{}' group by port having count(*)>=1) as interface where interface.mac like '{}%'".format(
                            bridge[0], bridge[1][0:11]))
                    # print("select * from (select parent_ip,mac,type,port from mib.topology_hardware where parent_ip!='{}' group by port having count(*)>=1) as interface where interface.mac like '{}%'".format(bridge[0],bridge[1][0:12]))
                    possible_parent = self.cursor.fetchone()
                    if possible_parent == None:
                        continue
                    else:
                        dict_rt, status = self.addSwitchToSecondLevel(dict_rt, dict_sw[key], possible_parent[0])
                        if status:
                            list_remove_switches.append(key)
        dict_sw = self.removeBridgedSwitchFromDict(list_remove_switches, dict_sw)
        return dict_rt, dict_sw

    def addSwitchToSecondLevel(self, dict_rt, switch, parent_ip):
        for key in dict_rt:
            for s_swich in dict_rt[key]["child"]:
                if s_swich["ip"] == parent_ip:
                    s_swich["child"].append(switch)
                    return dict_rt, True
        return dict_rt, False

    def getSwitchIPs(self, dict_sw):
        ip_list = []
        for key in dict_sw:
            ip_list.append(dict_sw[key]["ip"])
        return ip_list

    # Returns overall calculated topology of network
    def getTopology(self):
        is_complete = True
        dict_rt, int_ip_rt, int_sp_rt = self.getRouterTopology()
        dict_sw, int_ip_sw, int_sp_sw = self.getSwitchTopology()
        pprint.pprint(dict_sw)
        dict_rt, dict_sw = self.addRouterSwitchBridges(dict_rt, dict_sw)
        pprint.pprint(dict_sw)
        dict_rt, dict_sw = self.addSwitchSwitchBridges(dict_rt, dict_sw)
        # print("RouterSwitch Topology")
        # pprint.pprint(dict_rt)
        # print("Remaining Switches..")
        # pprint.pprint(dict_sw)
        return dict_rt

    # find all the router in a network returns json
    def getRouterTopology(self):
        dict = {}
        interface_ip = {}
        interface_speed = {}
        self.cursor.execute("SELECT hostname,host_bits FROM mib.topology_ssh where type='Router'")
        routers = self.cursor.fetchall()
        i = 1
        for router in routers:
            str_i = str(i)
            dict[str_i] = {}
            dict[str_i]["ip"] = []
            dict[str_i]["type"] = "router"
            i = i + 1
            self.cursor.execute("SELECT * FROM mib.topology_devices where parent_ip='{}' and age='-'".format(router[0]))
            interfaces = self.cursor.fetchall()
            for interface in interfaces:
                dict[str_i]["ip"].append(interface[1])
                interface_ip[interface[1]] = interface[4]
                interface_speed[interface[1]] = str(self.getInterfaceSpeedIntRouter(interface[4]))
            dict[str_i]["speed"] = "1000"
            dict[str_i]["mac"] = "MULTIPLE"
            dict[str_i]["child"] = []
        # print(dict)
        return dict, interface_ip, interface_speed

    # Get all the switches in the network and add corresponding connecting devices to it
    def getSwitchTopology(self):
        dict = {}
        interface_ip = {}
        interface_speed = {}
        self.cursor.execute("SELECT hostname,host_bits FROM mib.topology_ssh where type='Switch'")
        switchs = self.cursor.fetchall()
        i = 1
        for switch in switchs:
            str_i = str(i)
            dict[str_i] = {}
            dict[str_i]["ip"] = switch[0]
            dict[str_i]["type"] = "switch"
            dict[str_i]["speed"] = "1000"
            dict[str_i]["mac"] = "MULTIPLE"  # Work on this mac should be displayed
            dict[str_i]["child"] = []
            i = i + 1
            # Todo Fix type: it should be hardware and vlan and interface isnot showing
            self.cursor.execute(
                "SELECT mac,port FROM mib.topology_hardware where parent_ip='{}' group by port having count(*)<=1".format(
                    switch[0]))
            macs = self.cursor.fetchall()
            for mac in macs:
                self.cursor.execute(
                    "SELECT child_ip,parent_ip FROM mib.topology_devices where hard_address='{}' and parent_type='Router' and age!='-'".format(
                        mac[0]))
                devices = self.cursor.fetchall()
                for device in devices:
                    if self.areInSameNetwork(switch[0], device[0], switch[1]) and self.isNotASwithcIP(device[0],
                                                                                                      switchs):
                        temp = {"type": "device", "mac": str(mac[0]), "speed": "100", "ip": device[0],
                                "interface": mac[1]}
                        dict[str_i]["child"].append(temp)
                        interface_ip[device[0]] = mac[1]
                        interface_speed[device[0]] = str(self.getInterfaceSpeedIntSwitch(mac[1]))
        return dict, interface_ip, interface_speed

    # this combines the switches and router topology
    def addRouterSwitchBridges(self, dict_rt, dict_sw):
        # print("Adding router to switch bridges...")
        # this list contains the names of switch who have been bridged with routers and neet to be removed
        switch_remove_list = []
        self.cursor.execute("SELECT hostname,host_bits FROM mib.topology_ssh where type='Switch'")
        switches = self.cursor.fetchall()
        self.cursor.execute(
            "SELECT child_ip,age,hard_address,interface,parent_ip FROM mib.topology_devices where age='-' and parent_type='Router'")
        routers = self.cursor.fetchall()
        for switch in switches:
            for key in dict_sw:
                # switch(hostname/ip,host_bits)topology_ssh
                if switch[0] == dict_sw[key]["ip"]:
                    for router in routers:
                        # router(child_ip,age,mac,interface,parent_ip)topology_devices
                        if self.areInSameNetwork(router[0], switch[0], switch[1]) and router[1] == '-':
                            self.cursor.execute("select port from topology_hardware where parent_ip='{}' and mac='{}'".format(switch[0],router[2]))
                            port = self.cursor.fetchone()
                            if port != None:
                                self.cursor.execute("select * from topology_hardware where parent_ip='{}' and port='{}'".format(switch[0],port[0]))
                                port_int = self.cursor.fetchall()
                                port_count = len(port_int)
                                if port_count > 1:
                                    continue
                            dict_sw[key]["interface"] = router[3]
                            dict_sw[key]["mac"] = router[2]
                            dict_sw[key]["speed"] = self.getInterfaceSpeedIntRouter(router[3])
                            dict_rt = self.getAddSwitchToRouter(dict_rt, dict_sw[key], router[0])
                            switch_remove_list.append(key)
        dict_sw = self.removeBridgedSwitchFromDict(switch_remove_list, dict_sw)
        return dict_rt, dict_sw

    # parameters = router_of_all_dict,switch to be added,interface_of_router
    def removeBridgedSwitchFromDict(self, list, dict):
        for key in list:
            del dict[key]
        return dict

    def getAddSwitchToRouter(self, routers, switch, rt_interface_ip):
        for key in routers:
            if rt_interface_ip in routers[key]["ip"]:
                routers[key]["child"].append(switch)
        return routers
