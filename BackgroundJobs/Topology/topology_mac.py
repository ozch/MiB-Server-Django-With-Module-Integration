#python libraries
import paramiko
import re
#external libraries
from .mysql_connection import MySQLConnection

def getSshCredentials():
    con = MySQLConnection().initConnection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM topology_ssh")
    cursor.close()
    con.close()
    #print("All SSH Devices:")
    result = cursor.fetchall() 
    return result
def getHardwareAddress():
    ssh_cred = getSshCredentials()
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
        host_type= str(cred[5])
        port =str(cred[4])
        if host_type.lower() == 'router':
            continue
        #print(hostname,username,password,host_type,port)
        try:
            #print("Trying to Contect with")
            #print(cred)
            #Connecting and Getting Data From Network Device
            ssh.connect(hostname, port, username, password, look_for_keys=False)
            #ssh.exec_command('ping 192.168.1.0')
            stdin,stdout,stderr = ssh.exec_command('show mac address-table')
            output = stdout.readlines()
            s = "\n".join(output)
            ssh.close()
        except:
            #print("Connection Failed : Oops Something Went Wrong!!\n")
            ssh.close()
            continue
        line= iter(s.splitlines())
        for i in line:
            if(i=='' or i.startswith("       ") or i.endswith('Ports') or i.startswith("----") or i.startswith("Total Mac")):
                continue
            else:
                token = re.sub('\s+', ';',i).strip().split(";")
                query = "INSERT INTO mib.topology_hardware(parent_ip,vlan,mac,type,port)VALUES('{}','{}','{}','{}','{}')".format(hostname,token[1],token[2],token[3],token[4])
                cursorx.execute(query)
    conx.commit()
    cursorx.close()