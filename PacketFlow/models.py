from django.db import models


class Netflow(models.Model):
    version = models.IntegerField()
    reporter = models.PositiveIntegerField()
    src_id = models.PositiveSmallIntegerField()
    time_offset = models.PositiveIntegerField()
    in_bytes = models.BigIntegerField(blank=True, null=True)
    input_snmp = models.PositiveIntegerField(blank=True, null=True)
    layer2packetsectionoffset = models.PositiveIntegerField(blank=True, null=True)
    layer2packetsectionsize = models.PositiveIntegerField(blank=True, null=True)
    layer2packetsectiondata = models.PositiveIntegerField(blank=True, null=True)
    l4_dst_port = models.PositiveSmallIntegerField(blank=True, null=True)
    ipv4_dst_addr = models.PositiveIntegerField(blank=True, null=True)
    dst_mask = models.PositiveIntegerField(blank=True, null=True)
    output_snmp = models.PositiveIntegerField(blank=True, null=True)
    ipv4_next_hop = models.PositiveIntegerField(blank=True, null=True)
    src_as = models.PositiveIntegerField(blank=True, null=True)
    dst_as = models.PositiveIntegerField(blank=True, null=True)
    bgp_ipv4_next_hop = models.PositiveIntegerField(blank=True, null=True)
    mul_dst_pkts = models.PositiveIntegerField(blank=True, null=True)
    in_pkts = models.BigIntegerField(blank=True, null=True)
    mul_dst_bytes = models.PositiveIntegerField(blank=True, null=True)
    last_switched = models.PositiveIntegerField(blank=True, null=True)
    first_switched = models.PositiveIntegerField(blank=True, null=True)
    out_bytes = models.PositiveIntegerField(blank=True, null=True)
    out_pkts = models.PositiveIntegerField(blank=True, null=True)
    min_pkt_lngth = models.PositiveSmallIntegerField(blank=True, null=True)
    max_pkt_lngth = models.PositiveSmallIntegerField(blank=True, null=True)
    ipv6_src_addr = models.CharField(max_length=16, blank=True, null=True)
    ipv6_dst_addr = models.CharField(max_length=16, blank=True, null=True)
    ipv6_src_mask = models.PositiveIntegerField(blank=True, null=True)
    flows = models.BigIntegerField(blank=True, null=True)
    ipv6_dst_mask = models.PositiveIntegerField(blank=True, null=True)
    ipv6_flow_label = models.PositiveIntegerField(blank=True, null=True)
    icmp_type = models.PositiveSmallIntegerField(blank=True, null=True)
    mul_igmp_type = models.PositiveIntegerField(blank=True, null=True)
    sampling_interval = models.PositiveIntegerField(blank=True, null=True)
    sampling_algorithm = models.PositiveIntegerField(blank=True, null=True)
    flow_active_timeout = models.PositiveSmallIntegerField(blank=True, null=True)
    flow_inactive_timeout = models.PositiveSmallIntegerField(blank=True, null=True)
    engine_type = models.PositiveIntegerField(blank=True, null=True)
    engine_id = models.PositiveIntegerField(blank=True, null=True)
    protocol = models.PositiveIntegerField(blank=True, null=True)
    total_bytes_exp = models.BigIntegerField(blank=True, null=True)
    total_pkts_exp = models.BigIntegerField(blank=True, null=True)
    total_flows_exp = models.BigIntegerField(blank=True, null=True)
    ipv4_src_prefix = models.PositiveIntegerField(blank=True, null=True)
    ipv4_dst_prefix = models.PositiveIntegerField(blank=True, null=True)
    mpls_top_label_type = models.PositiveIntegerField(blank=True, null=True)
    mpls_top_label_ip_addr = models.PositiveIntegerField(blank=True, null=True)
    flow_sampler_id = models.PositiveIntegerField(blank=True, null=True)
    flow_sampler_mode = models.PositiveIntegerField(blank=True, null=True)
    src_tos = models.PositiveIntegerField(blank=True, null=True)
    flow_sampler_random_interval = models.PositiveIntegerField(blank=True, null=True)
    min_ttl = models.PositiveIntegerField(blank=True, null=True)
    max_ttl = models.PositiveIntegerField(blank=True, null=True)
    ipv4_ident = models.PositiveSmallIntegerField(blank=True, null=True)
    dst_tos = models.PositiveIntegerField(blank=True, null=True)
    in_src_mac = models.BigIntegerField(blank=True, null=True)
    out_dst_mac = models.BigIntegerField(blank=True, null=True)
    src_vlan = models.PositiveSmallIntegerField(blank=True, null=True)
    dst_vlan = models.PositiveSmallIntegerField(blank=True, null=True)
    tcp_flags = models.PositiveIntegerField(blank=True, null=True)
    ip_protocol_version = models.PositiveIntegerField(blank=True, null=True)
    direction = models.PositiveIntegerField(blank=True, null=True)
    ipv6_next_hop = models.CharField(max_length=16, blank=True, null=True)
    bgp_ipv6_next_hop = models.CharField(max_length=16, blank=True, null=True)
    ipv6_option_headers = models.PositiveIntegerField(blank=True, null=True)
    l4_src_port = models.PositiveSmallIntegerField(blank=True, null=True)
    mpls_label_1 = models.PositiveIntegerField(blank=True, null=True)
    mpls_label_2 = models.PositiveIntegerField(blank=True, null=True)
    mpls_label_3 = models.PositiveIntegerField(blank=True, null=True)
    mpls_label_4 = models.PositiveIntegerField(blank=True, null=True)
    mpls_label_5 = models.PositiveIntegerField(blank=True, null=True)
    mpls_label_6 = models.PositiveIntegerField(blank=True, null=True)
    mpls_label_7 = models.PositiveIntegerField(blank=True, null=True)
    mpls_label_8 = models.PositiveIntegerField(blank=True, null=True)
    mpls_label_9 = models.PositiveIntegerField(blank=True, null=True)
    mpls_label_10 = models.PositiveIntegerField(blank=True, null=True)
    ipv4_src_addr = models.PositiveIntegerField(blank=True, null=True)
    in_dst_mac = models.BigIntegerField(blank=True, null=True)
    out_src_mac = models.BigIntegerField(blank=True, null=True)
    if_name = models.CharField(max_length=80, blank=True, null=True)
    if_desc = models.CharField(max_length=256, blank=True, null=True)
    sampler_name = models.CharField(max_length=256, blank=True, null=True)
    in_permanent_bytes = models.BigIntegerField(blank=True, null=True)
    in_permanent_pkts = models.BigIntegerField(blank=True, null=True)
    fragment_offset = models.PositiveSmallIntegerField(blank=True, null=True)
    forwarding_status = models.PositiveIntegerField(blank=True, null=True)
    src_mask = models.PositiveIntegerField(blank=True, null=True)
    mpls_pal_rd = models.BigIntegerField(blank=True, null=True)
    mpls_prefix_len = models.PositiveIntegerField(blank=True, null=True)
    src_traffic_index = models.PositiveIntegerField(blank=True, null=True)
    dst_traffic_index = models.PositiveIntegerField(blank=True, null=True)
    application_description = models.CharField(max_length=256, blank=True, null=True)
    application_tag = models.CharField(max_length=256, blank=True, null=True)
    application_name = models.CharField(max_length=256, blank=True, null=True)
    postipdiffservcodepoint = models.PositiveIntegerField(blank=True, null=True)
    replication_factor = models.PositiveIntegerField(blank=True, null=True)
    ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'netflow'

    def __str__(self):
        return "Src : {}  ---  Dest : {}  ---  Pkts : {}  ---  Bytes : {}   ".format(self.ipv4_src_addr,
                                                                                     self.ipv6_dst_addr, self.in_pkts,
                                                                                     self.in_bytes)


# Created from view don't change
class NetflowV(models.Model):
    id = models.IntegerField(primary_key=True)
    version = models.IntegerField()
    reporter = models.PositiveIntegerField()
    src_id = models.PositiveSmallIntegerField()
    time_offset = models.PositiveIntegerField()
    in_bytes = models.BigIntegerField(blank=True, null=True)
    input_snmp = models.PositiveIntegerField(blank=True, null=True)
    layer2packetsectionoffset = models.PositiveIntegerField(blank=True, null=True)
    layer2packetsectionsize = models.PositiveIntegerField(blank=True, null=True)
    layer2packetsectiondata = models.PositiveIntegerField(blank=True, null=True)
    l4_dst_port = models.PositiveSmallIntegerField(blank=True, null=True)
    ipv4_dst_addr = models.PositiveIntegerField(blank=True, null=True)
    dst_mask = models.PositiveIntegerField(blank=True, null=True)
    output_snmp = models.PositiveIntegerField(blank=True, null=True)
    ipv4_next_hop = models.PositiveIntegerField(blank=True, null=True)
    src_as = models.PositiveIntegerField(blank=True, null=True)
    dst_as = models.PositiveIntegerField(blank=True, null=True)
    bgp_ipv4_next_hop = models.PositiveIntegerField(blank=True, null=True)
    mul_dst_pkts = models.PositiveIntegerField(blank=True, null=True)
    in_pkts = models.BigIntegerField(blank=True, null=True)
    mul_dst_bytes = models.PositiveIntegerField(blank=True, null=True)
    last_switched = models.PositiveIntegerField(blank=True, null=True)
    first_switched = models.PositiveIntegerField(blank=True, null=True)
    out_bytes = models.PositiveIntegerField(blank=True, null=True)
    out_pkts = models.PositiveIntegerField(blank=True, null=True)
    min_pkt_lngth = models.PositiveSmallIntegerField(blank=True, null=True)
    max_pkt_lngth = models.PositiveSmallIntegerField(blank=True, null=True)
    ipv6_src_addr = models.CharField(max_length=16, blank=True, null=True)
    ipv6_dst_addr = models.CharField(max_length=16, blank=True, null=True)
    ipv6_src_mask = models.PositiveIntegerField(blank=True, null=True)
    flows = models.BigIntegerField(blank=True, null=True)
    ipv6_dst_mask = models.PositiveIntegerField(blank=True, null=True)
    ipv6_flow_label = models.PositiveIntegerField(blank=True, null=True)
    icmp_type = models.PositiveSmallIntegerField(blank=True, null=True)
    mul_igmp_type = models.PositiveIntegerField(blank=True, null=True)
    sampling_interval = models.PositiveIntegerField(blank=True, null=True)
    sampling_algorithm = models.PositiveIntegerField(blank=True, null=True)
    flow_active_timeout = models.PositiveSmallIntegerField(blank=True, null=True)
    flow_inactive_timeout = models.PositiveSmallIntegerField(blank=True, null=True)
    engine_type = models.PositiveIntegerField(blank=True, null=True)
    engine_id = models.PositiveIntegerField(blank=True, null=True)
    protocol = models.PositiveIntegerField(blank=True, null=True)
    total_bytes_exp = models.BigIntegerField(blank=True, null=True)
    total_pkts_exp = models.BigIntegerField(blank=True, null=True)
    total_flows_exp = models.BigIntegerField(blank=True, null=True)
    ipv4_src_prefix = models.PositiveIntegerField(blank=True, null=True)
    ipv4_dst_prefix = models.PositiveIntegerField(blank=True, null=True)
    mpls_top_label_type = models.PositiveIntegerField(blank=True, null=True)
    mpls_top_label_ip_addr = models.PositiveIntegerField(blank=True, null=True)
    flow_sampler_id = models.PositiveIntegerField(blank=True, null=True)
    flow_sampler_mode = models.PositiveIntegerField(blank=True, null=True)
    src_tos = models.PositiveIntegerField(blank=True, null=True)
    flow_sampler_random_interval = models.PositiveIntegerField(blank=True, null=True)
    min_ttl = models.PositiveIntegerField(blank=True, null=True)
    max_ttl = models.PositiveIntegerField(blank=True, null=True)
    ipv4_ident = models.PositiveSmallIntegerField(blank=True, null=True)
    dst_tos = models.PositiveIntegerField(blank=True, null=True)
    in_src_mac = models.BigIntegerField(blank=True, null=True)
    out_dst_mac = models.BigIntegerField(blank=True, null=True)
    src_vlan = models.PositiveSmallIntegerField(blank=True, null=True)
    dst_vlan = models.PositiveSmallIntegerField(blank=True, null=True)
    tcp_flags = models.PositiveIntegerField(blank=True, null=True)
    ip_protocol_version = models.PositiveIntegerField(blank=True, null=True)
    direction = models.PositiveIntegerField(blank=True, null=True)
    ipv6_next_hop = models.CharField(max_length=16, blank=True, null=True)
    bgp_ipv6_next_hop = models.CharField(max_length=16, blank=True, null=True)
    ipv6_option_headers = models.PositiveIntegerField(blank=True, null=True)
    l4_src_port = models.PositiveSmallIntegerField(blank=True, null=True)
    mpls_label_1 = models.PositiveIntegerField(blank=True, null=True)
    mpls_label_2 = models.PositiveIntegerField(blank=True, null=True)
    mpls_label_3 = models.PositiveIntegerField(blank=True, null=True)
    mpls_label_4 = models.PositiveIntegerField(blank=True, null=True)
    mpls_label_5 = models.PositiveIntegerField(blank=True, null=True)
    mpls_label_6 = models.PositiveIntegerField(blank=True, null=True)
    mpls_label_7 = models.PositiveIntegerField(blank=True, null=True)
    mpls_label_8 = models.PositiveIntegerField(blank=True, null=True)
    mpls_label_9 = models.PositiveIntegerField(blank=True, null=True)
    mpls_label_10 = models.PositiveIntegerField(blank=True, null=True)
    ipv4_src_addr = models.PositiveIntegerField(blank=True, null=True)
    in_dst_mac = models.BigIntegerField(blank=True, null=True)
    out_src_mac = models.BigIntegerField(blank=True, null=True)
    if_name = models.CharField(max_length=80, blank=True, null=True)
    if_desc = models.CharField(max_length=256, blank=True, null=True)
    sampler_name = models.CharField(max_length=256, blank=True, null=True)
    in_permanent_bytes = models.BigIntegerField(blank=True, null=True)
    in_permanent_pkts = models.BigIntegerField(blank=True, null=True)
    fragment_offset = models.PositiveSmallIntegerField(blank=True, null=True)
    forwarding_status = models.PositiveIntegerField(blank=True, null=True)
    src_mask = models.PositiveIntegerField(blank=True, null=True)
    mpls_pal_rd = models.BigIntegerField(blank=True, null=True)
    mpls_prefix_len = models.PositiveIntegerField(blank=True, null=True)
    src_traffic_index = models.PositiveIntegerField(blank=True, null=True)
    dst_traffic_index = models.PositiveIntegerField(blank=True, null=True)
    application_description = models.CharField(max_length=256, blank=True, null=True)
    application_tag = models.CharField(max_length=256, blank=True, null=True)
    application_name = models.CharField(max_length=256, blank=True, null=True)
    postipdiffservcodepoint = models.PositiveIntegerField(blank=True, null=True)
    replication_factor = models.PositiveIntegerField(blank=True, null=True)
    reporter_a = models.CharField(max_length=31, blank=True, null=True)
    ipv4_src_addr_a = models.CharField(max_length=31, blank=True, null=True)
    ipv4_dst_addr_a = models.CharField(max_length=31, blank=True, null=True)
    ipv4_next_hop_a = models.CharField(max_length=31, blank=True, null=True)
    bgp_ipv4_next_hop_a = models.CharField(max_length=31, blank=True, null=True)
    ipv4_src_prefix_a = models.CharField(max_length=31, blank=True, null=True)
    ipv4_dst_prefix_a = models.CharField(max_length=31, blank=True, null=True)
    src_dscp = models.BigIntegerField(blank=True, null=True)
    dst_dscp = models.BigIntegerField(blank=True, null=True)
    first_switched_d = models.DateTimeField(blank=True, null=True)
    last_switched_d = models.DateTimeField(blank=True, null=True)
    tcp_flags_fin = models.BigIntegerField(blank=True, null=True)
    tcp_flags_syn = models.BigIntegerField(blank=True, null=True)
    tcp_flags_rst = models.BigIntegerField(blank=True, null=True)
    tcp_flags_psh = models.BigIntegerField(blank=True, null=True)
    tcp_flags_ack = models.BigIntegerField(blank=True, null=True)
    tcp_flags_urg = models.BigIntegerField(blank=True, null=True)
    ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'netflow_v'

    def __str__(self):
        return "Src : {}  ---  Dest : {}  ---  Pkts : {}  ---  Bytes : {}   ".format(self.ipv4_src_addr,
                                                                                     self.ipv6_dst_addr, self.in_pkts,
                                                                                     self.in_bytes)
