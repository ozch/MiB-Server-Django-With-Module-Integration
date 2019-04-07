from django.db import models
from django_mysql.models import JSONField


class TopologyBridge(models.Model):
    ip = models.CharField(max_length=100, blank=True, null=True)
    bridge = models.CharField(max_length=100, blank=True, null=True)
    vlan = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topology_bridge'

    def __str__(self):
        return "DeviceIP:{}--- Bridge:{} ".format(self.ip, self.bridge)


class TopologyDevices(models.Model):
    child_ip = models.CharField(max_length=50, blank=True, null=True)
    age = models.CharField(max_length=50, blank=True, null=True)
    hard_address = models.CharField(max_length=50, blank=True, null=True)
    interface = models.CharField(max_length=100, blank=True, null=True)
    parent_ip = models.CharField(max_length=50, blank=True, null=True)
    parent_type = models.CharField(max_length=50, blank=True, null=True)
    protocol = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topology_devices'

    def __str__(self):
        return "ChildIP : {}  ---  Age : {}  ---  Mac : {}  ---  Parent_IP : {}  ".format(self.child_ip, self.age,
                                                                                          self.hard_address,
                                                                                          self.parent_ip)


class TopologyHardware(models.Model):
    parent_ip = models.CharField(max_length=45, blank=True, null=True)
    vlan = models.CharField(max_length=45, blank=True, null=True)
    mac = models.CharField(max_length=45, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    port = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topology_hardware'

    def __str__(self):
        return "ParentIP : {}  ---  Mac : {}  ---  Type : {}  ---  Port : {}   ".format(self.parent_ip, self.mac,
                                                                                        self.type, self.port)


class TopologySsh(models.Model):
    hostname = models.CharField(unique=True, max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    port = models.CharField(max_length=10)
    type = models.CharField(max_length=45, blank=True, null=True)
    host_bits = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topology_ssh'

    def __str__(self):
        return "Hostname/IP : {}   ---  Port : {}  ---  Type : {}  ---  NetworkBits : {}".format(self.hostname,
                                                                                                 self.port, self.type,
                                                                                                 self.host_bits)
