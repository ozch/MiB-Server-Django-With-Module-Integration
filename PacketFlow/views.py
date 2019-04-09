from django.shortcuts import render
from .models import NetflowV
from django.utils import timezone
from BackgroundJobs.Topology.topology_graph import *
from django.http import JsonResponse
from singleton import Singleton
import math

config = Singleton
tg = TopologyGraph()


def Visualization(request):
    context = {'topology': config.topology,
               'intervel_ms': int(config.pktflw_vis_intervel) * 1000,
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
    print(flows.count())
    for flow in flows:
        start = flow.ipv4_src_addr_a
        end = flow.ipv4_dst_addr_a
        exporter = end = flow.reporter_a
        path = tg.find_path(graph, start, end, None, exporter)
        try:
            path.pop(0)
        except:
            continue
        net_flow.append({"start": start,
                         "packets": math.ceil(int(flow.in_pkts) / int(config.pktflw_vis_pkt_eql)) + 1,
                         "dest_port": flow.l4_dst_port,
                         "path": tg.RemoveRedundentRouterIPs(config.routers_interfaces, path)
                         })

    return JsonResponse(data=net_flow, safe=False)
