import nmap
import pprint


nm = nmap.PortScanner()
ipaddress = '192.168.1.1'
dict = nm.scan(hosts=ipaddress ,arguments='nmap -sV --script=sniffer-detect '+ipaddress)

pprint.pprint(dict['scan'])