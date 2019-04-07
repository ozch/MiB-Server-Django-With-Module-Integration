from django.shortcuts import render
from .models import NetflowV
from django.utils import timezone
from BackgroundJobs.Topology.topology_graph import *
from django.http import JsonResponse
from singleton import Singleton
import math
import pprint

config = Singleton
tg = TopologyGraph()


def Visualization(request):
    context = {'topology': config.topology,
               'intervel_ms': int(config.pktflw_vis_intervel) * 1000
               }

    return render(request=request, template_name='visualization.html', context=context)


def VizTopology(request):
    return JsonResponse(config.topology)


def PacketFlow(request):
    net_flow = []
    graph = config.path_graph
    now = timezone.now()
    print(type(config.pktflw_vis_intervel), config.pktflw_vis_intervel)
    int_sec = int(config.pktflw_vis_intervel)
    reference_time = now - timezone.timedelta(seconds=int_sec)
    flows = NetflowV.objects.filter(ts__gte=reference_time)
    flows = NetflowV.objects.filter(ipv4_dst_addr_a='192.168.1.1')
    print(flows.count())
    for flow in flows:
        start = flow.ipv4_src_addr_a
        end = flow.ipv4_dst_addr_a
        path = tg.find_path(graph, start, end)
        try:
            path.pop(0)
        except:
            continue
        net_flow.append({"start": start,
                         "packets": math.ceil(int(flow.in_pkts) / int(config.pktflw_vis_pkt_eql)) + 1,
                         "dest_port": flow.l4_dst_port,
                         "path": path
                         })
        pprint.pprint(net_flow)
        path = tg.find_path(graph, start, '192.168.1.3')
        path.pop(0)
        net_flow.append({"start": start,
                         "packets": math.ceil(int(flow.in_pkts) / int(config.pktflw_vis_pkt_eql)) + 1,
                         "dest_port": 11,
                         "path": path
                         })
        pprint.pprint(net_flow)

    return JsonResponse(data=net_flow, safe=False)


# Create your views here.


def PacketFlowFirst():
    net_flow = []
    graph = config.path_graph
    now = timezone.now()
    print(type(config.pktflw_vis_intervel), config.pktflw_vis_intervel)
    int_sec = int(config.pktflw_vis_intervel)
    reference_time = now - timezone.timedelta(seconds=int_sec)
    flows = NetflowV.objects.filter(ts__gte=reference_time)
    flows = NetflowV.objects.filter(ipv4_dst_addr_a='192.168.1.1')
    print(flows.count())
    for flow in flows:
        start = flow.ipv4_src_addr_a
        end = flow.ipv4_dst_addr_a
        path = tg.find_path(graph, start, end)
        try:
            path.pop(0)
        except:
            continue
        net_flow.append({"start": start,
                         "packets": math.ceil(int(flow.in_pkts) / int(config.pktflw_vis_pkt_eql)) + 1,
                         "dest_port": flow.l4_dst_port,
                         "path": path
                         })

    return net_flow
