query = "select id,version,reporter_a,ipv4_src_addr_a,ipv4_dst_addr_a,ipv4_next_hop_a,in_bytes,in_pkts,protocol,l4_src_port,l4_dst_port,src_mask,dst_mask,tcp_flags,direction,timediff(last_switched_d,first_switched_d) as time from mib.netflow_v"
from singleton import Singleton
config = Singleton
print(config.routers_interfaces)