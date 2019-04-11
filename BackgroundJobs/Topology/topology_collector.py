# python libraries
import paramiko
import re
import pprint
import traceback
import time

# external libraries
from .mysql_connection import MySQLConnection


class TopologyCollector():
    def getSshCredentials(self):
        con = MySQLConnection().initConnection()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM topology_ssh")
        cursor.close()
        con.close()
        print("Getting network device credentials...")
        result = cursor.fetchall()
        return result

    def collectRawNetwokData(self):
        self.getAllNetworkDevices()
        self.getHardwareAddress()

    def getAllNetworkDevices(self):
        print("Getting network device and network bridges...")
        ssh_cred = self.getSshCredentials()
        conx = MySQLConnection().initConnection()
        cursorx = conx.cursor()
        cursorx.execute("TRUNCATE TABLE mib.topology_devices")
        cursorx.execute("TRUNCATE TABLE mib.topology_bridge")
        for cred in ssh_cred:
            dict = {}
            bridge_vlan = {}
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            hostname = str(cred[1])
            username = str(cred[2])
            password = str(cred[3])
            host_type = str(cred[5])
            port = str(cred[4])
            print(hostname, username, password, host_type, port)
            try:
                print("Trying to contect with {}...".format(str(hostname)))
                ssh.connect(hostname, port, username, password, look_for_keys=False,timeout=30)
                stdin, stdout, stderr = ssh.exec_command('show ip arp')
                output = stdout.readlines()
                s = "\n".join(output)
                ssh.close()
            except Exception:
                traceback.print_exc()
                print("Connection Failure : Oops something went while trying to connect.\n")
                ssh.close()
                continue
            line = iter(s.splitlines())
            for i in line:
                if (i == '' or i.startswith('Protocol')):
                    continue
                else:
                    temp = re.sub('\s+', ';', i).strip().split(";")
                    dict[temp[1]] = {}
                    dict[temp[1]]['protocol'] = temp[0]
                    dict[temp[1]]['age'] = temp[2]
                    dict[temp[1]]['hard_addess'] = temp[3]
                    dict[temp[1]]['type'] = temp[4]
                    dict[temp[1]]['interface'] = temp[5]
                    dict[temp[1]]['parent'] = hostname
                    dict[temp[1]]['parent_type'] = host_type
                    query = "INSERT INTO mib.topology_devices (child_ip,age,hard_address,interface,parent_ip,parent_type,protocol,type) VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(
                        temp[1], temp[2], temp[3], temp[5], hostname, host_type, temp[0], temp[4])
                    cursorx.execute(query)
            if (cred[5].lower() == 'router'):  # if it's a router skip
                continue
            try:
                print("Getting devices bridge infromation...")
                # Connecting and Getting Data From Network Device
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname, port, username, password, look_for_keys=False)
                # ssh.exec_command('ping 192.168.1.0')
                chan = ssh.invoke_shell()
                chan.send('en\n')
                time.sleep(1)
                resp = chan.recv(9999)
                chan.send('ciscoen\n')
                time.sleep(1)
                resp = chan.recv(9999)
                stdout = chan.send('show spanning-tree bridge address\n')
                time.sleep(1)
                resp = chan.recv(9999)
                bridge = resp.decode("utf-8")
                ssh.close()
            except Exception:
                print("Connection Failure : Oops something went while trying to connect.\n")
                traceback.print_exc()
                ssh.close()
                continue
            bline = iter(bridge.splitlines())
            for i in bline:
                if 'show spanning-tree' in i or '#' in i:
                    continue
                temp = re.sub('\s+', ';', i).strip().split(";")
                print(temp)
                query = "INSERT INTO mib.topology_bridge(ip,bridge,vlan,type)VALUES('{}','{}','{}','{}')".format(
                    cred[1], temp[1], temp[0], cred[5])
                cursorx.execute(query)
            pprint.pprint(dict)
        conx.commit()
        cursorx.close()

    def getHardwareAddress(self):
        ssh_cred = self.getSshCredentials()
        conx = MySQLConnection().initConnection()
        cursorx = conx.cursor()
        cursorx.execute("TRUNCATE TABLE mib.topology_hardware")
        for cred in ssh_cred:
            dict = {}
            bridge_vlan = {}
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            hostname = str(cred[1])
            username = str(cred[2])
            password = str(cred[3])
            host_type = str(cred[5])
            port = str(cred[4])
            if host_type.lower() == 'router':
                continue
            print(hostname, username, password, host_type, port)
            try:
                print("Trying to contect with {}...".format(str(hostname)))
                # Connecting and Getting Data From Network Device
                ssh.connect(hostname, port, username, password, look_for_keys=False)
                # ssh.exec_command('ping 192.168.1.0')
                stdin, stdout, stderr = ssh.exec_command('show mac address-table')
                output = stdout.readlines()
                s = "\n".join(output)
                ssh.close()
            except Exception:
                print("Connection Failure : Oops something went while trying to connect.\n")
                traceback.print_exc()
                ssh.close()
                continue
            line = iter(s.splitlines())
            for i in line:
                if (i == '' or i.startswith("       ") or i.endswith('Ports') or i.startswith("----") or i.startswith(
                        "Total Mac")):
                    continue
                else:
                    token = re.sub('\s+', ';', i).strip().split(";")
                    query = "INSERT INTO mib.topology_hardware(parent_ip,vlan,mac,type,port)VALUES('{}','{}','{}','{}','{}')".format(
                        hostname, token[1], token[2], token[3], token[4])
                    cursorx.execute(query)
        conx.commit()
        cursorx.close()
