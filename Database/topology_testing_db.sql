/*mib schema structure*/;

truncate topology_bridge;
LOCK TABLES `topology_bridge` WRITE;
/*!40000 ALTER TABLE `topology_bridge` DISABLE KEYS */;
INSERT INTO `topology_bridge` VALUES (1,'192.168.1.2','5c50.15ff.4c80','VLAN0001','Switch'),(2,'192.168.1.3','5c50.15cd.ee00','VLAN0001','Switch');
/*!40000 ALTER TABLE `topology_bridge` ENABLE KEYS */;
UNLOCK TABLES;
truncate topology_devices;
LOCK TABLES `topology_devices` WRITE;
/*!40000 ALTER TABLE `topology_devices` DISABLE KEYS */;
INSERT INTO `topology_devices` VALUES (1,'192.168.1.10','0','a01d.48b6.69d7','Vlan1','192.168.1.2','Switch','Internet','ARPA'),(2,'192.168.1.2','-','5c50.15ff.4cc0','Vlan1','192.168.1.2','Switch','Internet','ARPA'),(3,'192.168.0.1','-','f872.ead0.bb82','GigabitEthernet0/2','192.168.1.1','Router','Internet','ARPA'),(4,'192.168.1.1','-','f872.ead0.bb80','GigabitEthernet0/0','192.168.1.1','Router','Internet','ARPA'),(5,'192.168.1.10','0','a01d.48b6.69d7','GigabitEthernet0/0','192.168.1.1','Router','Internet','ARPA'),(6,'192.168.2.1','-','f872.ead0.bb81','GigabitEthernet0/1','192.168.1.1','Router','Internet','ARPA'),(7,'192.168.1.10','0','a01d.48b6.69d7','Vlan1','192.168.1.3','Switch','Internet','ARPA'),(8,'192.168.1.3','-','5c50.15cd.ee40','Vlan1','192.168.1.3','Switch','Internet','ARPA');
/*!40000 ALTER TABLE `topology_devices` ENABLE KEYS */;
UNLOCK TABLES;
truncate topology_hardware;
LOCK TABLES `topology_hardware` WRITE;
/*!40000 ALTER TABLE `topology_hardware` DISABLE KEYS */;
INSERT INTO `topology_hardware` VALUES (1,'192.168.1.2','All','0100.0ccc.cccc','STATIC','CPU'),(2,'192.168.1.2','All','0100.0ccc.cccd','STATIC','CPU'),(3,'192.168.1.2','All','0180.c200.0000','STATIC','CPU'),(4,'192.168.1.2','All','0180.c200.0001','STATIC','CPU'),(5,'192.168.1.2','All','0180.c200.0002','STATIC','CPU'),(6,'192.168.1.2','All','0180.c200.0003','STATIC','CPU'),(7,'192.168.1.2','All','0180.c200.0004','STATIC','CPU'),(8,'192.168.1.2','All','0180.c200.0005','STATIC','CPU'),(9,'192.168.1.2','All','0180.c200.0006','STATIC','CPU'),(10,'192.168.1.2','All','0180.c200.0007','STATIC','CPU'),(11,'192.168.1.2','All','0180.c200.0008','STATIC','CPU'),(12,'192.168.1.2','All','0180.c200.0009','STATIC','CPU'),(13,'192.168.1.2','All','0180.c200.000a','STATIC','CPU'),(14,'192.168.1.2','All','0180.c200.000b','STATIC','CPU'),(15,'192.168.1.2','All','0180.c200.000c','STATIC','CPU'),(16,'192.168.1.2','All','0180.c200.000d','STATIC','CPU'),(17,'192.168.1.2','All','0180.c200.000e','STATIC','CPU'),(18,'192.168.1.2','All','0180.c200.000f','STATIC','CPU'),(19,'192.168.1.2','All','0180.c200.0010','STATIC','CPU'),(20,'192.168.1.2','All','ffff.ffff.ffff','STATIC','CPU'),(21,'192.168.1.2','1','5c50.15cd.ee09','DYNAMIC','Fa0/7'),(22,'192.168.1.2','1','5c50.15cd.ee40','DYNAMIC','Fa0/7'),(23,'192.168.1.2','1','a01d.48b6.69d7','DYNAMIC','Fa0/27'),(24,'192.168.1.2','1','f872.ead0.bb80','DYNAMIC','Fa0/11'),(25,'192.168.1.3','All','0100.0ccc.cccc','STATIC','CPU'),(26,'192.168.1.3','All','0100.0ccc.cccd','STATIC','CPU'),(27,'192.168.1.3','All','0180.c200.0000','STATIC','CPU'),(28,'192.168.1.3','All','0180.c200.0001','STATIC','CPU'),(29,'192.168.1.3','All','0180.c200.0002','STATIC','CPU'),(30,'192.168.1.3','All','0180.c200.0003','STATIC','CPU'),(31,'192.168.1.3','All','0180.c200.0004','STATIC','CPU'),(32,'192.168.1.3','All','0180.c200.0005','STATIC','CPU'),(33,'192.168.1.3','All','0180.c200.0006','STATIC','CPU'),(34,'192.168.1.3','All','0180.c200.0007','STATIC','CPU'),(35,'192.168.1.3','All','0180.c200.0008','STATIC','CPU'),(36,'192.168.1.3','All','0180.c200.0009','STATIC','CPU'),(37,'192.168.1.3','All','0180.c200.000a','STATIC','CPU'),(38,'192.168.1.3','All','0180.c200.000b','STATIC','CPU'),(39,'192.168.1.3','All','0180.c200.000c','STATIC','CPU'),(40,'192.168.1.3','All','0180.c200.000d','STATIC','CPU'),(41,'192.168.1.3','All','0180.c200.000e','STATIC','CPU'),(42,'192.168.1.3','All','0180.c200.000f','STATIC','CPU'),(43,'192.168.1.3','All','0180.c200.0010','STATIC','CPU'),(44,'192.168.1.3','All','ffff.ffff.ffff','STATIC','CPU'),(45,'192.168.1.3','1','5c50.15ff.4c87','DYNAMIC','Fa0/9'),(46,'192.168.1.3','1','a01d.48b6.69d7','DYNAMIC','Fa0/9'),(47,'192.168.1.3','1','f872.ead0.bb80','DYNAMIC','Fa0/9');
/*!40000 ALTER TABLE `topology_hardware` ENABLE KEYS */;
UNLOCK TABLES;
truncate topology_ssh;
LOCK TABLES `topology_ssh` WRITE;
/*!40000 ALTER TABLE `topology_ssh` DISABLE KEYS */;
INSERT INTO `topology_ssh` VALUES (2,'192.168.1.2','admin','cisco','22','Switch','24'),(3,'192.168.1.1','admin','cisco','22','Router','24'),(4,'192.168.1.3','admin','cisco','22','Switch','24');
/*!40000 ALTER TABLE `topology_ssh` ENABLE KEYS */;
UNLOCK TABLES;

/*#####################################################*/;
/*topology not working*/;

truncate topology_bridge;
LOCK TABLES `topology_bridge` WRITE;
/*!40000 ALTER TABLE `topology_bridge` DISABLE KEYS */;
INSERT INTO `topology_bridge` VALUES (1,'192.168.1.2','5c50.15ff.4c80','VLAN0001','Switch'),(2,'192.168.0.2','5c50.15cd.ee00','VLAN0001','Switch');
/*!40000 ALTER TABLE `topology_bridge` ENABLE KEYS */;
UNLOCK TABLES;
truncate topology_devices;
LOCK TABLES `topology_devices` WRITE;
/*!40000 ALTER TABLE `topology_devices` DISABLE KEYS */;
INSERT INTO `topology_devices` VALUES (1,'192.168.1.10','0','507b.9d79.9bcc','Vlan1','192.168.1.2','Switch','Internet','ARPA'),(2,'192.168.1.2','-','5c50.15ff.4cc0','Vlan1','192.168.1.2','Switch','Internet','ARPA'),(3,'192.168.0.1','-','f872.ead0.bb82','GigabitEthernet0/2','192.168.1.1','Router','Internet','ARPA'),(4,'192.168.1.1','-','f872.ead0.bb80','GigabitEthernet0/0','192.168.1.1','Router','Internet','ARPA'),(5,'192.168.1.10','0','507b.9d79.9bcc','GigabitEthernet0/0','192.168.1.1','Router','Internet','ARPA'),(6,'192.168.2.1','-','f872.ead0.bb81','GigabitEthernet0/1','192.168.1.1','Router','Internet','ARPA'),(7,'192.168.0.10','0','Incomplete','','192.168.0.2','Switch','Internet','ARPA'),(8,'192.168.1.10','0','f872.ead0.bb82','Vlan1','192.168.0.2','Switch','Internet','ARPA'),(9,'192.168.0.2','-','5c50.15cd.ee40','Vlan1','192.168.0.2','Switch','Internet','ARPA');
/*!40000 ALTER TABLE `topology_devices` ENABLE KEYS */;
UNLOCK TABLES;
truncate topology_hardware;
LOCK TABLES `topology_hardware` WRITE;
/*!40000 ALTER TABLE `topology_hardware` DISABLE KEYS */;
INSERT INTO `topology_hardware` VALUES (1,'192.168.1.2','All','0100.0ccc.cccc','STATIC','CPU'),(2,'192.168.1.2','All','0100.0ccc.cccd','STATIC','CPU'),(3,'192.168.1.2','All','0180.c200.0000','STATIC','CPU'),(4,'192.168.1.2','All','0180.c200.0001','STATIC','CPU'),(5,'192.168.1.2','All','0180.c200.0002','STATIC','CPU'),(6,'192.168.1.2','All','0180.c200.0003','STATIC','CPU'),(7,'192.168.1.2','All','0180.c200.0004','STATIC','CPU'),(8,'192.168.1.2','All','0180.c200.0005','STATIC','CPU'),(9,'192.168.1.2','All','0180.c200.0006','STATIC','CPU'),(10,'192.168.1.2','All','0180.c200.0007','STATIC','CPU'),(11,'192.168.1.2','All','0180.c200.0008','STATIC','CPU'),(12,'192.168.1.2','All','0180.c200.0009','STATIC','CPU'),(13,'192.168.1.2','All','0180.c200.000a','STATIC','CPU'),(14,'192.168.1.2','All','0180.c200.000b','STATIC','CPU'),(15,'192.168.1.2','All','0180.c200.000c','STATIC','CPU'),(16,'192.168.1.2','All','0180.c200.000d','STATIC','CPU'),(17,'192.168.1.2','All','0180.c200.000e','STATIC','CPU'),(18,'192.168.1.2','All','0180.c200.000f','STATIC','CPU'),(19,'192.168.1.2','All','0180.c200.0010','STATIC','CPU'),(20,'192.168.1.2','All','ffff.ffff.ffff','STATIC','CPU'),(21,'192.168.1.2','1','507b.9d79.9bcc','DYNAMIC','Fa0/12'),(22,'192.168.1.2','1','f872.ead0.bb80','DYNAMIC','Fa0/2'),(23,'192.168.0.2','All','0100.0ccc.cccc','STATIC','CPU'),(24,'192.168.0.2','All','0100.0ccc.cccd','STATIC','CPU'),(25,'192.168.0.2','All','0180.c200.0000','STATIC','CPU'),(26,'192.168.0.2','All','0180.c200.0001','STATIC','CPU'),(27,'192.168.0.2','All','0180.c200.0002','STATIC','CPU'),(28,'192.168.0.2','All','0180.c200.0003','STATIC','CPU'),(29,'192.168.0.2','All','0180.c200.0004','STATIC','CPU'),(30,'192.168.0.2','All','0180.c200.0005','STATIC','CPU'),(31,'192.168.0.2','All','0180.c200.0006','STATIC','CPU'),(32,'192.168.0.2','All','0180.c200.0007','STATIC','CPU'),(33,'192.168.0.2','All','0180.c200.0008','STATIC','CPU'),(34,'192.168.0.2','All','0180.c200.0009','STATIC','CPU'),(35,'192.168.0.2','All','0180.c200.000a','STATIC','CPU'),(36,'192.168.0.2','All','0180.c200.000b','STATIC','CPU'),(37,'192.168.0.2','All','0180.c200.000c','STATIC','CPU'),(38,'192.168.0.2','All','0180.c200.000d','STATIC','CPU'),(39,'192.168.0.2','All','0180.c200.000e','STATIC','CPU'),(40,'192.168.0.2','All','0180.c200.000f','STATIC','CPU'),(41,'192.168.0.2','All','0180.c200.0010','STATIC','CPU'),(42,'192.168.0.2','All','ffff.ffff.ffff','STATIC','CPU'),(43,'192.168.0.2','1','f872.ead0.bb82','DYNAMIC','Fa0/2');
/*!40000 ALTER TABLE `topology_hardware` ENABLE KEYS */;
UNLOCK TABLES;
truncate topology_ssh;
LOCK TABLES `topology_ssh` WRITE;
/*!40000 ALTER TABLE `topology_ssh` DISABLE KEYS */;
INSERT INTO `topology_ssh` VALUES (2,'192.168.1.2','admin','cisco','22','Switch','24'),(3,'192.168.1.1','admin','cisco','22','Router','24'),(4,'192.168.0.2','admin','cisco','22','Switch','24');
/*!40000 ALTER TABLE `topology_ssh` ENABLE KEYS */;
UNLOCK TABLES;


/*=============================================*/;
/*where i fucked up*/


truncate topology_bridge;
LOCK TABLES `topology_bridge` WRITE;
/*!40000 ALTER TABLE `topology_bridge` DISABLE KEYS */;
INSERT INTO `topology_bridge` VALUES (1,'192.168.1.2','5c50.15ff.4c80','VLAN0001','Switch'),(2,'192.168.0.2','5c50.15cd.ee00','VLAN0001','Switch');
/*!40000 ALTER TABLE `topology_bridge` ENABLE KEYS */;
UNLOCK TABLES;
truncate topology_devices;
LOCK TABLES `topology_devices` WRITE;
/*!40000 ALTER TABLE `topology_devices` DISABLE KEYS */;
INSERT INTO `topology_devices` VALUES (1,'192.168.0.11','14','f872.ead0.bb80','Vlan1','192.168.1.2','Switch','Internet','ARPA'),(2,'192.168.1.10','8','507b.9d79.9bcc','Vlan1','192.168.1.2','Switch','Internet','ARPA'),(3,'192.168.1.2','-','5c50.15ff.4cc0','Vlan1','192.168.1.2','Switch','Internet','ARPA'),(4,'192.168.0.1','-','f872.ead0.bb82','GigabitEthernet0/2','192.168.1.1','Router','Internet','ARPA'),(5,'192.168.0.2','26','5c50.15cd.ee40','GigabitEthernet0/2','192.168.1.1','Router','Internet','ARPA'),(6,'192.168.0.11','3','b82a.72b8.4197','GigabitEthernet0/2','192.168.1.1','Router','Internet','ARPA'),(7,'192.168.0.187','0','001e.3753.6e88','GigabitEthernet0/2','192.168.1.1','Router','Internet','ARPA'),(8,'192.168.1.1','-','f872.ead0.bb80','GigabitEthernet0/0','192.168.1.1','Router','Internet','ARPA'),(9,'192.168.1.2','14','5c50.15ff.4cc0','GigabitEthernet0/0','192.168.1.1','Router','Internet','ARPA'),(10,'192.168.1.10','8','507b.9d79.9bcc','GigabitEthernet0/0','192.168.1.1','Router','Internet','ARPA'),(11,'192.168.1.11','30','b82a.72b8.4197','GigabitEthernet0/0','192.168.1.1','Router','Internet','ARPA'),(12,'192.168.2.1','-','f872.ead0.bb81','GigabitEthernet0/1','192.168.1.1','Router','Internet','ARPA'),(13,'192.168.0.11','14','b82a.72b8.4197','Vlan1','192.168.0.2','Switch','Internet','ARPA'),(14,'192.168.1.10','41','f872.ead0.bb82','Vlan1','192.168.0.2','Switch','Internet','ARPA'),(15,'192.168.0.2','-','5c50.15cd.ee40','Vlan1','192.168.0.2','Switch','Internet','ARPA');
/*!40000 ALTER TABLE `topology_devices` ENABLE KEYS */;
UNLOCK TABLES;
truncate topology_hardware;
LOCK TABLES `topology_hardware` WRITE;
/*!40000 ALTER TABLE `topology_hardware` DISABLE KEYS */;
INSERT INTO `topology_hardware` VALUES (1,'192.168.1.2','All','0100.0ccc.cccc','STATIC','CPU'),(2,'192.168.1.2','All','0100.0ccc.cccd','STATIC','CPU'),(3,'192.168.1.2','All','0180.c200.0000','STATIC','CPU'),(4,'192.168.1.2','All','0180.c200.0001','STATIC','CPU'),(5,'192.168.1.2','All','0180.c200.0002','STATIC','CPU'),(6,'192.168.1.2','All','0180.c200.0003','STATIC','CPU'),(7,'192.168.1.2','All','0180.c200.0004','STATIC','CPU'),(8,'192.168.1.2','All','0180.c200.0005','STATIC','CPU'),(9,'192.168.1.2','All','0180.c200.0006','STATIC','CPU'),(10,'192.168.1.2','All','0180.c200.0007','STATIC','CPU'),(11,'192.168.1.2','All','0180.c200.0008','STATIC','CPU'),(12,'192.168.1.2','All','0180.c200.0009','STATIC','CPU'),(13,'192.168.1.2','All','0180.c200.000a','STATIC','CPU'),(14,'192.168.1.2','All','0180.c200.000b','STATIC','CPU'),(15,'192.168.1.2','All','0180.c200.000c','STATIC','CPU'),(16,'192.168.1.2','All','0180.c200.000d','STATIC','CPU'),(17,'192.168.1.2','All','0180.c200.000e','STATIC','CPU'),(18,'192.168.1.2','All','0180.c200.000f','STATIC','CPU'),(19,'192.168.1.2','All','0180.c200.0010','STATIC','CPU'),(20,'192.168.1.2','All','ffff.ffff.ffff','STATIC','CPU'),(21,'192.168.1.2','1','507b.9d79.9bcc','DYNAMIC','Fa0/12'),(22,'192.168.1.2','1','f872.ead0.bb80','DYNAMIC','Fa0/2'),(23,'192.168.0.2','All','0100.0ccc.cccc','STATIC','CPU'),(24,'192.168.0.2','All','0100.0ccc.cccd','STATIC','CPU'),(25,'192.168.0.2','All','0180.c200.0000','STATIC','CPU'),(26,'192.168.0.2','All','0180.c200.0001','STATIC','CPU'),(27,'192.168.0.2','All','0180.c200.0002','STATIC','CPU'),(28,'192.168.0.2','All','0180.c200.0003','STATIC','CPU'),(29,'192.168.0.2','All','0180.c200.0004','STATIC','CPU'),(30,'192.168.0.2','All','0180.c200.0005','STATIC','CPU'),(31,'192.168.0.2','All','0180.c200.0006','STATIC','CPU'),(32,'192.168.0.2','All','0180.c200.0007','STATIC','CPU'),(33,'192.168.0.2','All','0180.c200.0008','STATIC','CPU'),(34,'192.168.0.2','All','0180.c200.0009','STATIC','CPU'),(35,'192.168.0.2','All','0180.c200.000a','STATIC','CPU'),(36,'192.168.0.2','All','0180.c200.000b','STATIC','CPU'),(37,'192.168.0.2','All','0180.c200.000c','STATIC','CPU'),(38,'192.168.0.2','All','0180.c200.000d','STATIC','CPU'),(39,'192.168.0.2','All','0180.c200.000e','STATIC','CPU'),(40,'192.168.0.2','All','0180.c200.000f','STATIC','CPU'),(41,'192.168.0.2','All','001e.3753.6e88','STATIC','Fa0/7'),(42,'192.168.0.2','All','ffff.ffff.ffff','STATIC','Fa0/7'),(43,'192.168.0.2','1','001e.3753.6e88','DYNAMIC','Fa0/8'),(44,'192.168.0.2','1','b82a.72b8.4197','DYNAMIC','Fa0/19'),(45,'192.168.0.2','1','f872.ead0.bb82','DYNAMIC','Fa0/2');
/*!40000 ALTER TABLE `topology_hardware` ENABLE KEYS */;
UNLOCK TABLES;
truncate topology_ssh;
LOCK TABLES `topology_ssh` WRITE;
/*!40000 ALTER TABLE `topology_ssh` DISABLE KEYS */;
INSERT INTO `topology_ssh` VALUES (2,'192.168.1.2','admin','cisco','22','Switch','24'),(3,'192.168.1.1','admin','cisco','22','Router','24'),(4,'192.168.0.2','admin','cisco','22','Switch','24');
/*!40000 ALTER TABLE `topology_ssh` ENABLE KEYS */;
UNLOCK TABLES;
