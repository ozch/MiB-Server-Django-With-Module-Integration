CREATE DATABASE  IF NOT EXISTS `mib` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `mib`;
-- MySQL dump 10.13  Distrib 5.7.25, for Win64 (x86_64)
--
-- Host: localhost    Database: mib
-- ------------------------------------------------------
-- Server version	5.7.25-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `background_task`
--

DROP TABLE IF EXISTS `background_task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `background_task` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_name` varchar(190) NOT NULL,
  `task_params` longtext NOT NULL,
  `task_hash` varchar(40) NOT NULL,
  `verbose_name` varchar(255) DEFAULT NULL,
  `priority` int(11) NOT NULL,
  `run_at` datetime(6) NOT NULL,
  `repeat` bigint(20) NOT NULL,
  `repeat_until` datetime(6) DEFAULT NULL,
  `queue` varchar(190) DEFAULT NULL,
  `attempts` int(11) NOT NULL,
  `failed_at` datetime(6) DEFAULT NULL,
  `last_error` longtext NOT NULL,
  `locked_by` varchar(64) DEFAULT NULL,
  `locked_at` datetime(6) DEFAULT NULL,
  `creator_object_id` int(10) unsigned DEFAULT NULL,
  `creator_content_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `background_task_creator_content_type_61cc9af3_fk_django_co` (`creator_content_type_id`),
  KEY `background_task_task_name_4562d56a` (`task_name`),
  KEY `background_task_task_hash_d8f233bd` (`task_hash`),
  KEY `background_task_priority_88bdbce9` (`priority`),
  KEY `background_task_run_at_7baca3aa` (`run_at`),
  KEY `background_task_queue_1d5f3a40` (`queue`),
  KEY `background_task_attempts_a9ade23d` (`attempts`),
  KEY `background_task_failed_at_b81bba14` (`failed_at`),
  KEY `background_task_locked_by_db7779e3` (`locked_by`),
  KEY `background_task_locked_at_0fb0f225` (`locked_at`),
  CONSTRAINT `background_task_creator_content_type_61cc9af3_fk_django_co` FOREIGN KEY (`creator_content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=363 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `background_task_completedtask`
--

DROP TABLE IF EXISTS `background_task_completedtask`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `background_task_completedtask` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `task_name` varchar(190) NOT NULL,
  `task_params` longtext NOT NULL,
  `task_hash` varchar(40) NOT NULL,
  `verbose_name` varchar(255) DEFAULT NULL,
  `priority` int(11) NOT NULL,
  `run_at` datetime(6) NOT NULL,
  `repeat` bigint(20) NOT NULL,
  `repeat_until` datetime(6) DEFAULT NULL,
  `queue` varchar(190) DEFAULT NULL,
  `attempts` int(11) NOT NULL,
  `failed_at` datetime(6) DEFAULT NULL,
  `last_error` longtext NOT NULL,
  `locked_by` varchar(64) DEFAULT NULL,
  `locked_at` datetime(6) DEFAULT NULL,
  `creator_object_id` int(10) unsigned DEFAULT NULL,
  `creator_content_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `background_task_comp_creator_content_type_21d6a741_fk_django_co` (`creator_content_type_id`),
  KEY `background_task_completedtask_task_name_388dabc2` (`task_name`),
  KEY `background_task_completedtask_task_hash_91187576` (`task_hash`),
  KEY `background_task_completedtask_priority_9080692e` (`priority`),
  KEY `background_task_completedtask_run_at_77c80f34` (`run_at`),
  KEY `background_task_completedtask_queue_61fb0415` (`queue`),
  KEY `background_task_completedtask_attempts_772a6783` (`attempts`),
  KEY `background_task_completedtask_failed_at_3de56618` (`failed_at`),
  KEY `background_task_completedtask_locked_by_edc8a213` (`locked_by`),
  KEY `background_task_completedtask_locked_at_29c62708` (`locked_at`),
  CONSTRAINT `background_task_comp_creator_content_type_21d6a741_fk_django_co` FOREIGN KEY (`creator_content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=399 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `device_info`
--

DROP TABLE IF EXISTS `device_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `device_info` (
  `mac_address` varchar(12) NOT NULL,
  `ip_address` varchar(20) DEFAULT NULL,
  `mask` varchar(20) DEFAULT NULL,
  `sys_info` json DEFAULT NULL,
  PRIMARY KEY (`mac_address`),
  UNIQUE KEY `mac_address_UNIQUE` (`mac_address`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `execute`
--

DROP TABLE IF EXISTS `execute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `execute` (
  `mac_address` varchar(12) NOT NULL,
  `boot_flag` int(11) NOT NULL DEFAULT '0',
  `service_flag` int(11) NOT NULL DEFAULT '0',
  `kill_flag` int(11) NOT NULL DEFAULT '0',
  `script_flag` int(11) NOT NULL DEFAULT '0',
  `port_flag` int(11) NOT NULL DEFAULT '0',
  `boot_command` varchar(10) DEFAULT 'DONE',
  `service_name` varchar(50) DEFAULT 'DONE',
  `kill_name` varchar(50) DEFAULT 'DONE',
  `script` longtext,
  `portno` int(11) DEFAULT '4000',
  `online` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`mac_address`),
  UNIQUE KEY `mac_add_UNIQUE` (`mac_address`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ipc`
--

DROP TABLE IF EXISTS `ipc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ipc` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `mutex` int(11) DEFAULT '0',
  `topology` json DEFAULT NULL,
  `path_graph` json DEFAULT NULL,
  `network_devices` json DEFAULT NULL,
  `routers_interface` json DEFAULT NULL,
  `interface_list` json DEFAULT NULL,
  `interface_speed` json DEFAULT NULL,
  `updated` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `netflow`
--

DROP TABLE IF EXISTS `netflow`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `netflow` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `version` tinyint(4) NOT NULL,
  `reporter` int(10) unsigned NOT NULL,
  `src_id` smallint(5) unsigned NOT NULL,
  `time_offset` int(10) unsigned NOT NULL,
  `in_bytes` bigint(20) unsigned DEFAULT NULL,
  `input_snmp` int(10) unsigned DEFAULT NULL,
  `layer2packetsectionoffset` int(10) unsigned DEFAULT NULL,
  `layer2packetsectionsize` int(10) unsigned DEFAULT NULL,
  `layer2packetsectiondata` int(10) unsigned DEFAULT NULL,
  `l4_dst_port` smallint(5) unsigned DEFAULT NULL,
  `ipv4_dst_addr` int(10) unsigned DEFAULT NULL,
  `dst_mask` tinyint(3) unsigned DEFAULT NULL,
  `output_snmp` int(10) unsigned DEFAULT NULL,
  `ipv4_next_hop` int(10) unsigned DEFAULT NULL,
  `src_as` int(10) unsigned DEFAULT NULL,
  `dst_as` int(10) unsigned DEFAULT NULL,
  `bgp_ipv4_next_hop` int(10) unsigned DEFAULT NULL,
  `mul_dst_pkts` int(10) unsigned DEFAULT NULL,
  `in_pkts` bigint(20) unsigned DEFAULT NULL,
  `mul_dst_bytes` int(10) unsigned DEFAULT NULL,
  `last_switched` int(10) unsigned DEFAULT NULL,
  `first_switched` int(10) unsigned DEFAULT NULL,
  `out_bytes` int(10) unsigned DEFAULT NULL,
  `out_pkts` int(10) unsigned DEFAULT NULL,
  `min_pkt_lngth` smallint(5) unsigned DEFAULT NULL,
  `max_pkt_lngth` smallint(5) unsigned DEFAULT NULL,
  `ipv6_src_addr` varbinary(16) DEFAULT NULL,
  `ipv6_dst_addr` varbinary(16) DEFAULT NULL,
  `ipv6_src_mask` tinyint(3) unsigned DEFAULT NULL,
  `flows` bigint(20) unsigned DEFAULT NULL,
  `ipv6_dst_mask` tinyint(3) unsigned DEFAULT NULL,
  `ipv6_flow_label` int(10) unsigned DEFAULT NULL,
  `icmp_type` smallint(5) unsigned DEFAULT NULL,
  `mul_igmp_type` tinyint(3) unsigned DEFAULT NULL,
  `sampling_interval` int(10) unsigned DEFAULT NULL,
  `sampling_algorithm` tinyint(3) unsigned DEFAULT NULL,
  `flow_active_timeout` smallint(5) unsigned DEFAULT NULL,
  `flow_inactive_timeout` smallint(5) unsigned DEFAULT NULL,
  `engine_type` tinyint(3) unsigned DEFAULT NULL,
  `engine_id` tinyint(3) unsigned DEFAULT NULL,
  `protocol` tinyint(3) unsigned DEFAULT NULL,
  `total_bytes_exp` bigint(20) unsigned DEFAULT NULL,
  `total_pkts_exp` bigint(20) unsigned DEFAULT NULL,
  `total_flows_exp` bigint(20) unsigned DEFAULT NULL,
  `ipv4_src_prefix` int(10) unsigned DEFAULT NULL,
  `ipv4_dst_prefix` int(10) unsigned DEFAULT NULL,
  `mpls_top_label_type` tinyint(3) unsigned DEFAULT NULL,
  `mpls_top_label_ip_addr` int(10) unsigned DEFAULT NULL,
  `flow_sampler_id` tinyint(3) unsigned DEFAULT NULL,
  `flow_sampler_mode` tinyint(3) unsigned DEFAULT NULL,
  `src_tos` tinyint(3) unsigned DEFAULT NULL,
  `flow_sampler_random_interval` int(10) unsigned DEFAULT NULL,
  `min_ttl` tinyint(3) unsigned DEFAULT NULL,
  `max_ttl` tinyint(3) unsigned DEFAULT NULL,
  `ipv4_ident` smallint(5) unsigned DEFAULT NULL,
  `dst_tos` tinyint(3) unsigned DEFAULT NULL,
  `in_src_mac` bigint(20) unsigned DEFAULT NULL,
  `out_dst_mac` bigint(20) unsigned DEFAULT NULL,
  `src_vlan` smallint(5) unsigned DEFAULT NULL,
  `dst_vlan` smallint(5) unsigned DEFAULT NULL,
  `tcp_flags` tinyint(3) unsigned DEFAULT NULL,
  `ip_protocol_version` tinyint(3) unsigned DEFAULT NULL,
  `direction` tinyint(3) unsigned DEFAULT NULL,
  `ipv6_next_hop` binary(16) DEFAULT NULL,
  `bgp_ipv6_next_hop` binary(16) DEFAULT NULL,
  `ipv6_option_headers` int(10) unsigned DEFAULT NULL,
  `l4_src_port` smallint(5) unsigned DEFAULT NULL,
  `mpls_label_1` int(10) unsigned DEFAULT NULL,
  `mpls_label_2` int(10) unsigned DEFAULT NULL,
  `mpls_label_3` int(10) unsigned DEFAULT NULL,
  `mpls_label_4` int(10) unsigned DEFAULT NULL,
  `mpls_label_5` int(10) unsigned DEFAULT NULL,
  `mpls_label_6` int(10) unsigned DEFAULT NULL,
  `mpls_label_7` int(10) unsigned DEFAULT NULL,
  `mpls_label_8` int(10) unsigned DEFAULT NULL,
  `mpls_label_9` int(10) unsigned DEFAULT NULL,
  `mpls_label_10` int(10) unsigned DEFAULT NULL,
  `ipv4_src_addr` int(10) unsigned DEFAULT NULL,
  `in_dst_mac` bigint(20) unsigned DEFAULT NULL,
  `out_src_mac` bigint(20) unsigned DEFAULT NULL,
  `if_name` varbinary(80) DEFAULT NULL,
  `if_desc` varbinary(256) DEFAULT NULL,
  `sampler_name` varbinary(256) DEFAULT NULL,
  `in_permanent_bytes` bigint(20) unsigned DEFAULT NULL,
  `in_permanent_pkts` bigint(20) unsigned DEFAULT NULL,
  `fragment_offset` smallint(5) unsigned DEFAULT NULL,
  `forwarding_status` tinyint(3) unsigned DEFAULT NULL,
  `src_mask` tinyint(3) unsigned DEFAULT NULL,
  `mpls_pal_rd` bigint(20) unsigned DEFAULT NULL,
  `mpls_prefix_len` tinyint(3) unsigned DEFAULT NULL,
  `src_traffic_index` int(10) unsigned DEFAULT NULL,
  `dst_traffic_index` int(10) unsigned DEFAULT NULL,
  `application_description` varbinary(256) DEFAULT NULL,
  `application_tag` varbinary(256) DEFAULT NULL,
  `application_name` varbinary(256) DEFAULT NULL,
  `postipdiffservcodepoint` tinyint(3) unsigned DEFAULT NULL,
  `replication_factor` int(10) unsigned DEFAULT NULL,
  `ts` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `ts` (`ts`)
) ENGINE=InnoDB AUTO_INCREMENT=1847 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary table structure for view `netflow_v`
--

DROP TABLE IF EXISTS `netflow_v`;
/*!50001 DROP VIEW IF EXISTS `netflow_v`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `netflow_v` AS SELECT 
 1 AS `id`,
 1 AS `version`,
 1 AS `reporter`,
 1 AS `src_id`,
 1 AS `time_offset`,
 1 AS `in_bytes`,
 1 AS `input_snmp`,
 1 AS `layer2packetsectionoffset`,
 1 AS `layer2packetsectionsize`,
 1 AS `layer2packetsectiondata`,
 1 AS `l4_dst_port`,
 1 AS `ipv4_dst_addr`,
 1 AS `dst_mask`,
 1 AS `output_snmp`,
 1 AS `ipv4_next_hop`,
 1 AS `src_as`,
 1 AS `dst_as`,
 1 AS `bgp_ipv4_next_hop`,
 1 AS `mul_dst_pkts`,
 1 AS `in_pkts`,
 1 AS `mul_dst_bytes`,
 1 AS `last_switched`,
 1 AS `first_switched`,
 1 AS `out_bytes`,
 1 AS `out_pkts`,
 1 AS `min_pkt_lngth`,
 1 AS `max_pkt_lngth`,
 1 AS `ipv6_src_addr`,
 1 AS `ipv6_dst_addr`,
 1 AS `ipv6_src_mask`,
 1 AS `flows`,
 1 AS `ipv6_dst_mask`,
 1 AS `ipv6_flow_label`,
 1 AS `icmp_type`,
 1 AS `mul_igmp_type`,
 1 AS `sampling_interval`,
 1 AS `sampling_algorithm`,
 1 AS `flow_active_timeout`,
 1 AS `flow_inactive_timeout`,
 1 AS `engine_type`,
 1 AS `engine_id`,
 1 AS `protocol`,
 1 AS `total_bytes_exp`,
 1 AS `total_pkts_exp`,
 1 AS `total_flows_exp`,
 1 AS `ipv4_src_prefix`,
 1 AS `ipv4_dst_prefix`,
 1 AS `mpls_top_label_type`,
 1 AS `mpls_top_label_ip_addr`,
 1 AS `flow_sampler_id`,
 1 AS `flow_sampler_mode`,
 1 AS `src_tos`,
 1 AS `flow_sampler_random_interval`,
 1 AS `min_ttl`,
 1 AS `max_ttl`,
 1 AS `ipv4_ident`,
 1 AS `dst_tos`,
 1 AS `in_src_mac`,
 1 AS `out_dst_mac`,
 1 AS `src_vlan`,
 1 AS `dst_vlan`,
 1 AS `tcp_flags`,
 1 AS `ip_protocol_version`,
 1 AS `direction`,
 1 AS `ipv6_next_hop`,
 1 AS `bgp_ipv6_next_hop`,
 1 AS `ipv6_option_headers`,
 1 AS `l4_src_port`,
 1 AS `mpls_label_1`,
 1 AS `mpls_label_2`,
 1 AS `mpls_label_3`,
 1 AS `mpls_label_4`,
 1 AS `mpls_label_5`,
 1 AS `mpls_label_6`,
 1 AS `mpls_label_7`,
 1 AS `mpls_label_8`,
 1 AS `mpls_label_9`,
 1 AS `mpls_label_10`,
 1 AS `ipv4_src_addr`,
 1 AS `in_dst_mac`,
 1 AS `out_src_mac`,
 1 AS `if_name`,
 1 AS `if_desc`,
 1 AS `sampler_name`,
 1 AS `in_permanent_bytes`,
 1 AS `in_permanent_pkts`,
 1 AS `fragment_offset`,
 1 AS `forwarding_status`,
 1 AS `src_mask`,
 1 AS `mpls_pal_rd`,
 1 AS `mpls_prefix_len`,
 1 AS `src_traffic_index`,
 1 AS `dst_traffic_index`,
 1 AS `application_description`,
 1 AS `application_tag`,
 1 AS `application_name`,
 1 AS `postipdiffservcodepoint`,
 1 AS `replication_factor`,
 1 AS `ts`,
 1 AS `reporter_a`,
 1 AS `ipv4_src_addr_a`,
 1 AS `ipv4_dst_addr_a`,
 1 AS `ipv4_next_hop_a`,
 1 AS `bgp_ipv4_next_hop_a`,
 1 AS `ipv4_src_prefix_a`,
 1 AS `ipv4_dst_prefix_a`,
 1 AS `src_dscp`,
 1 AS `dst_dscp`,
 1 AS `first_switched_d`,
 1 AS `last_switched_d`,
 1 AS `tcp_flags_fin`,
 1 AS `tcp_flags_syn`,
 1 AS `tcp_flags_rst`,
 1 AS `tcp_flags_psh`,
 1 AS `tcp_flags_ack`,
 1 AS `tcp_flags_urg`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `network_open_port`
--

DROP TABLE IF EXISTS `network_open_port`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `network_open_port` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(40) NOT NULL,
  `ip_status` varchar(10) DEFAULT NULL,
  `port_type` varchar(10) DEFAULT NULL,
  `port_no` int(11) NOT NULL,
  `conf` varchar(100) DEFAULT NULL,
  `cpe` varchar(100) DEFAULT NULL,
  `extrainfo` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `product` varchar(100) DEFAULT NULL,
  `reason` varchar(100) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `version` varchar(100) DEFAULT NULL,
  `ts` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=311 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `network_sniffers`
--

DROP TABLE IF EXISTS `network_sniffers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `network_sniffers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(40) DEFAULT NULL,
  `is_sniffer` int(11) DEFAULT NULL,
  `predict` varchar(50) DEFAULT NULL,
  `remarks` varchar(200) DEFAULT NULL,
  `ts` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `open_ports`
--

DROP TABLE IF EXISTS `open_ports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `open_ports` (
  `mac_address` varchar(12) NOT NULL,
  `json` json DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  PRIMARY KEY (`mac_address`),
  UNIQUE KEY `mac_address_UNIQUE` (`mac_address`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `process_info`
--

DROP TABLE IF EXISTS `process_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `process_info` (
  `mac_address` varchar(12) NOT NULL,
  `process_info` json DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  PRIMARY KEY (`mac_address`),
  UNIQUE KEY `mac_address_UNIQUE` (`mac_address`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `services_info`
--

DROP TABLE IF EXISTS `services_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `services_info` (
  `mac_address` varchar(12) NOT NULL,
  `services_info` json DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  PRIMARY KEY (`mac_address`),
  UNIQUE KEY `mac_address_UNIQUE` (`mac_address`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `token`
--

DROP TABLE IF EXISTS `token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `token` (
  `token` varchar(100) NOT NULL,
  `mac` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`token`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `token_store`
--

DROP TABLE IF EXISTS `token_store`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `token_store` (
  `token` varchar(100) NOT NULL,
  `is_taken` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`token`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `topology_bridge`
--

DROP TABLE IF EXISTS `topology_bridge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `topology_bridge` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(100) DEFAULT NULL,
  `bridge` varchar(100) DEFAULT NULL,
  `vlan` varchar(100) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `topology_devices`
--

DROP TABLE IF EXISTS `topology_devices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `topology_devices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `child_ip` varchar(50) DEFAULT NULL,
  `age` varchar(50) DEFAULT NULL,
  `hard_address` varchar(50) DEFAULT NULL,
  `interface` varchar(100) DEFAULT NULL,
  `parent_ip` varchar(50) DEFAULT NULL,
  `parent_type` varchar(50) DEFAULT NULL,
  `protocol` varchar(100) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `topology_hardware`
--

DROP TABLE IF EXISTS `topology_hardware`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `topology_hardware` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `parent_ip` varchar(45) DEFAULT NULL,
  `vlan` varchar(45) DEFAULT NULL,
  `mac` varchar(45) DEFAULT NULL,
  `type` varchar(45) DEFAULT NULL,
  `port` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `topology_ssh`
--

DROP TABLE IF EXISTS `topology_ssh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `topology_ssh` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `port` varchar(10) NOT NULL,
  `type` varchar(45) DEFAULT 'NaN',
  `host_bits` varchar(45) DEFAULT '24',
  PRIMARY KEY (`id`),
  UNIQUE KEY `hostname_UNIQUE` (`hostname`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Final view structure for view `netflow_v`
--

/*!50001 DROP VIEW IF EXISTS `netflow_v`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `netflow_v` AS select `n`.`id` AS `id`,`n`.`version` AS `version`,`n`.`reporter` AS `reporter`,`n`.`src_id` AS `src_id`,`n`.`time_offset` AS `time_offset`,`n`.`in_bytes` AS `in_bytes`,`n`.`input_snmp` AS `input_snmp`,`n`.`layer2packetsectionoffset` AS `layer2packetsectionoffset`,`n`.`layer2packetsectionsize` AS `layer2packetsectionsize`,`n`.`layer2packetsectiondata` AS `layer2packetsectiondata`,`n`.`l4_dst_port` AS `l4_dst_port`,`n`.`ipv4_dst_addr` AS `ipv4_dst_addr`,`n`.`dst_mask` AS `dst_mask`,`n`.`output_snmp` AS `output_snmp`,`n`.`ipv4_next_hop` AS `ipv4_next_hop`,`n`.`src_as` AS `src_as`,`n`.`dst_as` AS `dst_as`,`n`.`bgp_ipv4_next_hop` AS `bgp_ipv4_next_hop`,`n`.`mul_dst_pkts` AS `mul_dst_pkts`,`n`.`in_pkts` AS `in_pkts`,`n`.`mul_dst_bytes` AS `mul_dst_bytes`,`n`.`last_switched` AS `last_switched`,`n`.`first_switched` AS `first_switched`,`n`.`out_bytes` AS `out_bytes`,`n`.`out_pkts` AS `out_pkts`,`n`.`min_pkt_lngth` AS `min_pkt_lngth`,`n`.`max_pkt_lngth` AS `max_pkt_lngth`,`n`.`ipv6_src_addr` AS `ipv6_src_addr`,`n`.`ipv6_dst_addr` AS `ipv6_dst_addr`,`n`.`ipv6_src_mask` AS `ipv6_src_mask`,`n`.`flows` AS `flows`,`n`.`ipv6_dst_mask` AS `ipv6_dst_mask`,`n`.`ipv6_flow_label` AS `ipv6_flow_label`,`n`.`icmp_type` AS `icmp_type`,`n`.`mul_igmp_type` AS `mul_igmp_type`,`n`.`sampling_interval` AS `sampling_interval`,`n`.`sampling_algorithm` AS `sampling_algorithm`,`n`.`flow_active_timeout` AS `flow_active_timeout`,`n`.`flow_inactive_timeout` AS `flow_inactive_timeout`,`n`.`engine_type` AS `engine_type`,`n`.`engine_id` AS `engine_id`,`n`.`protocol` AS `protocol`,`n`.`total_bytes_exp` AS `total_bytes_exp`,`n`.`total_pkts_exp` AS `total_pkts_exp`,`n`.`total_flows_exp` AS `total_flows_exp`,`n`.`ipv4_src_prefix` AS `ipv4_src_prefix`,`n`.`ipv4_dst_prefix` AS `ipv4_dst_prefix`,`n`.`mpls_top_label_type` AS `mpls_top_label_type`,`n`.`mpls_top_label_ip_addr` AS `mpls_top_label_ip_addr`,`n`.`flow_sampler_id` AS `flow_sampler_id`,`n`.`flow_sampler_mode` AS `flow_sampler_mode`,`n`.`src_tos` AS `src_tos`,`n`.`flow_sampler_random_interval` AS `flow_sampler_random_interval`,`n`.`min_ttl` AS `min_ttl`,`n`.`max_ttl` AS `max_ttl`,`n`.`ipv4_ident` AS `ipv4_ident`,`n`.`dst_tos` AS `dst_tos`,`n`.`in_src_mac` AS `in_src_mac`,`n`.`out_dst_mac` AS `out_dst_mac`,`n`.`src_vlan` AS `src_vlan`,`n`.`dst_vlan` AS `dst_vlan`,`n`.`tcp_flags` AS `tcp_flags`,`n`.`ip_protocol_version` AS `ip_protocol_version`,`n`.`direction` AS `direction`,`n`.`ipv6_next_hop` AS `ipv6_next_hop`,`n`.`bgp_ipv6_next_hop` AS `bgp_ipv6_next_hop`,`n`.`ipv6_option_headers` AS `ipv6_option_headers`,`n`.`l4_src_port` AS `l4_src_port`,`n`.`mpls_label_1` AS `mpls_label_1`,`n`.`mpls_label_2` AS `mpls_label_2`,`n`.`mpls_label_3` AS `mpls_label_3`,`n`.`mpls_label_4` AS `mpls_label_4`,`n`.`mpls_label_5` AS `mpls_label_5`,`n`.`mpls_label_6` AS `mpls_label_6`,`n`.`mpls_label_7` AS `mpls_label_7`,`n`.`mpls_label_8` AS `mpls_label_8`,`n`.`mpls_label_9` AS `mpls_label_9`,`n`.`mpls_label_10` AS `mpls_label_10`,`n`.`ipv4_src_addr` AS `ipv4_src_addr`,`n`.`in_dst_mac` AS `in_dst_mac`,`n`.`out_src_mac` AS `out_src_mac`,`n`.`if_name` AS `if_name`,`n`.`if_desc` AS `if_desc`,`n`.`sampler_name` AS `sampler_name`,`n`.`in_permanent_bytes` AS `in_permanent_bytes`,`n`.`in_permanent_pkts` AS `in_permanent_pkts`,`n`.`fragment_offset` AS `fragment_offset`,`n`.`forwarding_status` AS `forwarding_status`,`n`.`src_mask` AS `src_mask`,`n`.`mpls_pal_rd` AS `mpls_pal_rd`,`n`.`mpls_prefix_len` AS `mpls_prefix_len`,`n`.`src_traffic_index` AS `src_traffic_index`,`n`.`dst_traffic_index` AS `dst_traffic_index`,`n`.`application_description` AS `application_description`,`n`.`application_tag` AS `application_tag`,`n`.`application_name` AS `application_name`,`n`.`postipdiffservcodepoint` AS `postipdiffservcodepoint`,`n`.`replication_factor` AS `replication_factor`,`n`.`ts` AS `ts`,inet_ntoa(`n`.`reporter`) AS `reporter_a`,inet_ntoa(`n`.`ipv4_src_addr`) AS `ipv4_src_addr_a`,inet_ntoa(`n`.`ipv4_dst_addr`) AS `ipv4_dst_addr_a`,inet_ntoa(`n`.`ipv4_next_hop`) AS `ipv4_next_hop_a`,inet_ntoa(`n`.`bgp_ipv4_next_hop`) AS `bgp_ipv4_next_hop_a`,inet_ntoa(`n`.`ipv4_src_prefix`) AS `ipv4_src_prefix_a`,inet_ntoa(`n`.`ipv4_dst_prefix`) AS `ipv4_dst_prefix_a`,(`n`.`src_tos` >> 2) AS `src_dscp`,(`n`.`dst_tos` >> 2) AS `dst_dscp`,from_unixtime(((`n`.`first_switched` DIV 1000) + `n`.`time_offset`)) AS `first_switched_d`,from_unixtime(((`n`.`last_switched` DIV 1000) + `n`.`time_offset`)) AS `last_switched_d`,(`n`.`tcp_flags` & 1) AS `tcp_flags_fin`,((`n`.`tcp_flags` & 2) >> 1) AS `tcp_flags_syn`,((`n`.`tcp_flags` & 4) >> 2) AS `tcp_flags_rst`,((`n`.`tcp_flags` & 8) >> 3) AS `tcp_flags_psh`,((`n`.`tcp_flags` & 16) >> 4) AS `tcp_flags_ack`,((`n`.`tcp_flags` & 32) >> 5) AS `tcp_flags_urg` from `netflow` `n` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-11 18:16:46
