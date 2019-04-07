from django.db import models
from django_mysql.models import JSONField


class DeviceInfo(models.Model):
    mac_address = models.CharField(primary_key=True, max_length=12)
    ip_address = models.CharField(max_length=20, blank=True, null=True)
    mask = models.CharField(max_length=20, blank=True, null=True)
    sys_info = JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device_info'

    def __str__(self):
        return "Mac : {}  ---  IP:{}  ---  Mask : {}   (More details)".format(self.mac_address, self.ip_address,
                                                                              self.mask)


class Execute(models.Model):
    mac_address = models.CharField(primary_key=True, max_length=12)
    boot_flag = models.IntegerField()
    service_flag = models.IntegerField()
    kill_flag = models.IntegerField()
    script_flag = models.IntegerField()
    port_flag = models.IntegerField()
    boot_command = models.CharField(max_length=10, blank=True, null=True)
    service_name = models.CharField(max_length=50, blank=True, null=True)
    kill_name = models.CharField(max_length=50, blank=True, null=True)
    script = models.TextField(blank=True, null=True)
    portno = models.IntegerField(blank=True, null=True)
    online = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'execute'

    def __str__(self):
        return "Mac : {}  ---   LastOnline : {}".format(self.mac_address, self.online)


class OpenPorts(models.Model):
    mac_address = models.CharField(primary_key=True, max_length=12)
    json = JSONField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'open_ports'

    def __str__(self):
        return "Mac : {}  ---  OpenPorts : {}".format(self.mac_address, "Click for details.")


class ProcessInfo(models.Model):
    mac_address = models.CharField(primary_key=True, max_length=12)
    process_info = JSONField(blank=True, null=True)  # This field type is a guess.
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'process_info'

    def __str__(self):
        return "Mac : {}  ---  ProcessInfo : {}".format(self.mac_address, "Click for details.")


class ServicesInfo(models.Model):
    mac_address = models.CharField(primary_key=True, max_length=12)
    services_info = JSONField(blank=True, null=True)  # This field type is a guess.
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services_info'

    def __str__(self):
        return "Mac : {}  ---  ServiceInfo : {}".format(self.mac_address, "Click for details.")


class Token(models.Model):
    token = models.CharField(primary_key=True, max_length=100)
    mac = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'token'

    def __str__(self):
        return "Token : {}  ---  Mac : {}".format(self.token, self.mac)


class TokenStore(models.Model):
    token = models.CharField(primary_key=True, max_length=100)
    is_taken = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'token_store'

    def __str__(self):
        return "Token : {}  ---  isTaken : {}".format(self.token, self.is_taken)
