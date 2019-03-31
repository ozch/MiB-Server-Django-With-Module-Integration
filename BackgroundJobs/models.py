from django.db import models

class NetworkPortScanner(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=40)#future proofing for ipv6
    ip_status = models.CharField(max_length=10,null=True)
    port_type = models.CharField(max_length=10, blank=True, null=True)
    port_no = models.IntegerField()
    conf = models.CharField(max_length=100, blank=True, null=True)
    cpe = models.CharField(max_length=100, blank=True, null=True)
    extrainfo = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    product = models.CharField(max_length=100, blank=True, null=True)
    reason = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)
    ts = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = True
        db_table = 'network_open_port'
    def __str__(self):
        return "IP : {}  ---   Last_Scan_Time : {}".format(self.ip,self.ts)
class NetworkSnifferScanner(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=40,null=True)#future proofing for ipv6
    is_sniffer = models.IntegerField(null=True)
    predict = models.CharField(max_length=50,null=True)
    remarks = models.CharField(max_length=200,null=True)
    ts = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = True
        db_table = 'network_sniffers'
    def __str__(self):
        return "IP : {}  ---   Last_Scan_Time : {}".format(self.ip,self.ts)
