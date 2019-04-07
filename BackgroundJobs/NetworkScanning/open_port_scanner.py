import nmap
import sys
import socket
import time

# nmap -sV --script=sniffer-detect <target>
ipaddress = '127.0.0.1'
alpha = 1
omega = 6000
t1 = time.time()
portrange = "{}-{}".format(alpha, omega)
try:
    # initialize the port scanner
    scanner = nmap.PortScanner()  # instantiate nmap.PortScanner object
    scanner.scan(ipaddress, portrange)  # scan host which is specify & ports from 22 to 44
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
except:
    print("Unexpected error:", sys.exc_info()[0])
# run a loop to print all the found result about the ports
t2 = time.time()
print(t2 - t1)
for host in scanner.all_hosts():
    print("       Host : %s " % (host))
    print("       State : %s" % scanner[host].state())  # get state of host(up|down|unknown|skipped)
    # now write the loop for finding the protocol
    for proto in scanner[host].all_protocols():  # get all scanned protocols ['tcp', 'udp'] in (ip|tcp|udp|sctp)
        print("----------" * 6)
        print("       Protocol : %s" % proto)
        lport = scanner[host][proto].keys()  # get all ports for tcp/udp protocol
        for port in lport:
            print("       port : %s\tstate : %s" % (port, scanner[host][proto][port]['state']))
