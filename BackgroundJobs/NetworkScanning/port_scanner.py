import nmap
import pprint
from singleton import  Singleton
def PortScanner():
    config = Singleton
    devices = config.network_devices
    print("Port_Scanner>>",devices)
    nm = nmap.PortScanner()
    ipaddress = '192.168.1.20'
    dict = nm.scan(hosts=ipaddress ,arguments='nmap -sV --script=sniffer-detect '+ipaddress)
    pprint.pprint(dict['scan'])
    devices = config.network_devices