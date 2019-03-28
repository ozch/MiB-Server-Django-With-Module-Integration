from django.contrib import admin
from .models import *

admin.site.register(TopologyBridge)
admin.site.register(TopologyDevices)
admin.site.register(TopologyHardware)
admin.site.register(TopologySsh)