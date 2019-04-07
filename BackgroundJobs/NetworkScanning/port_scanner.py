import nmap
import pprint
import time
from datetime import datetime
from singleton import Singleton
from django.utils import timezone
from django.utils.timezone import activate
from MIBServer.settings import TIME_ZONE

activate(TIME_ZONE)

from BackgroundJobs.models import *


def PortScanner():
    config = Singleton
    devices = config.network_devices
    # print("Port_Scanner Devies List : ",devices)
    # Todo : remove this line its temprory
    devices = ['192.168.1.1', '192.168.1.20']
    for ip in devices:
        nm = nmap.PortScanner()
        ipaddress = ip
        dict = nm.scan(hosts=ipaddress, arguments='nmap -sV --script=sniffer-detect ' + ipaddress)
        # pprint.pprint(dict['scan'])
        # Todo : Add Exception Handling here
        if 'scan' in dict:
            AddOpenPortScanInformation(scan=dict['scan'], ip=ip)


def AddOpenPortScanInformation(scan, ip):
    for key in scan:
        if key == ip:
            temp_ip = ip
            temp_status = scan[key]['status']['state']
            if 'hostscript' in scan[key]:
                AddSnifferScanInformation(temp_ip, 1, scan[key]['hostscript'])
            else:
                AddSnifferScanInformation(temp_ip, 0, {})
            if 'tcp' in scan[key]:
                AddOpenPorts('tcp', temp_ip, temp_status, scan[key]['tcp'])
            if 'udp' in scan[key]:
                AddOpenPorts('tcp', temp_ip, temp_status, scan[key]['udp'])


def AddOpenPorts(type, ip, state, dict):
    NetworkPortScanner.objects.filter(ip=ip).delete()
    for key in dict:
        instance_ = NetworkPortScanner()
        instance_.ip = ip
        instance_.ip_status = state
        instance_.port_type = type
        instance_.conf = dict[key]['conf']
        instance_.cpe = dict[key]['cpe']
        instance_.extrainfo = dict[key]['extrainfo']
        instance_.name = dict[key]['name']
        instance_.product = dict[key]['product']
        instance_.reason = dict[key]['reason']
        instance_.state = dict[key]['state']
        instance_.version = dict[key]['version']
        instance_.ts = timezone.localtime(timezone.now())
        instance_.port_no = key
        instance_.save()


def AddSnifferScanInformation(ip, is_sniffer, scan):
    NetworkSnifferScanner.objects.filter(ip=ip).delete()
    instance_ = NetworkSnifferScanner()
    instance_.ip = ip
    instance_.is_sniffer = is_sniffer
    if is_sniffer == 1:
        instance_.remarks = scan[0]['output']
        instance_.predict = scan[0]['id']
        instance_.ts = timezone.localtime(timezone.now())
    else:
        instance_.remarks = "Null"
        instance_.predict = "Null"
        instance_.ts = timezone.localtime(timezone.now())
    instance_.save()
