from django.contrib import admin
from .models import *
admin.site.register(Token)
admin.site.register(TokenStore)
admin.site.register(DeviceInfo)
admin.site.register(Execute)
admin.site.register(OpenPorts)
admin.site.register(ServicesInfo)
admin.site.register(ProcessInfo)