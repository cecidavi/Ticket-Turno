/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.7.2-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: ticket_turno
-- ------------------------------------------------------
-- Server version	11.7.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `alumno`
--

DROP TABLE IF EXISTS `alumno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `alumno` (
  `curp` char(18) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `paterno` varchar(50) NOT NULL,
  `materno` varchar(50) NOT NULL,
  PRIMARY KEY (`curp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumno`
--

LOCK TABLES `alumno` WRITE;
/*!40000 ALTER TABLE `alumno` DISABLE KEYS */;
INSERT INTO `alumno` VALUES
('DBSK690807MTLJAP16','prueba8','prueba8','prueba8'),
('DPWX250315HCLMMF30','prueba6','prueba6','prueba6'),
('JAZY201021MQTYAT16','prueba4','prueba4','prueba4'),
('JZUU290913HQRQIH61','prueba2','prueba2','prueba22'),
('MFUL990818MPLISO84','pruebafinal','pruebafinal','pruebafinal'),
('QSFN951216HBCBVD50','prueba3','prueba3','prueba3'),
('SAHC020128HNLNRCA1','cecilio','sanchez','hernandez'),
('URHV030622HZSWPD27','prueba5','prueba5','prueba5'),
('WMDQ140227MMNUTX11','prueba7','prueba7','prueba7');
/*!40000 ALTER TABLE `alumno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asuntos`
--

DROP TABLE IF EXISTS `asuntos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `asuntos` (
  `id_asunto` int(11) NOT NULL AUTO_INCREMENT,
  `asunto` varchar(50) NOT NULL,
  PRIMARY KEY (`id_asunto`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asuntos`
--

LOCK TABLES `asuntos` WRITE;
/*!40000 ALTER TABLE `asuntos` DISABLE KEYS */;
INSERT INTO `asuntos` VALUES
(1,'Inscripción'),
(2,'Cambio de escuela'),
(3,'Baja'),
(4,'prueba'),
(6,'prueba2');
/*!40000 ALTER TABLE `asuntos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estatus`
--

DROP TABLE IF EXISTS `estatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `estatus` (
  `id_estatus` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_estatus` varchar(20) NOT NULL,
  PRIMARY KEY (`id_estatus`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estatus`
--

LOCK TABLES `estatus` WRITE;
/*!40000 ALTER TABLE `estatus` DISABLE KEYS */;
INSERT INTO `estatus` VALUES
(1,'Pendiente'),
(2,'Resuelto');
/*!40000 ALTER TABLE `estatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `municipios`
--

DROP TABLE IF EXISTS `municipios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `municipios` (
  `cve_mun` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_mun` varchar(50) NOT NULL,
  PRIMARY KEY (`cve_mun`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `municipios`
--

LOCK TABLES `municipios` WRITE;
/*!40000 ALTER TABLE `municipios` DISABLE KEYS */;
INSERT INTO `municipios` VALUES
(1,'Abasolo'),
(2,'Acuña'),
(3,'Allende'),
(4,'Arteaga'),
(5,'Candela'),
(6,'Castaños'),
(7,'Cuatro Ciénegas'),
(8,'Escobedo'),
(9,'Francisco I. Madero'),
(10,'Frontera'),
(11,'General Cepeda'),
(12,'Guerrero'),
(13,'Hidalgo'),
(14,'Jiménez'),
(15,'Juárez'),
(16,'Lamadrid'),
(17,'Matamoros'),
(18,'Monclova'),
(19,'Morelos'),
(20,'Múzquiz'),
(21,'Nadadores'),
(22,'Nava'),
(23,'Ocampo'),
(24,'Parras'),
(25,'Piedras Negras'),
(26,'Progreso'),
(27,'Ramos Arizpe'),
(28,'Sabinas'),
(29,'Sacramento'),
(30,'Saltillo'),
(31,'San Buenaventura'),
(32,'San Juan de Sabinas'),
(33,'San Pedro'),
(34,'Sierra Mojada'),
(35,'Torreón'),
(36,'Viesca'),
(37,'Villa Unión'),
(38,'Zaragoza'),
(39,'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA');
/*!40000 ALTER TABLE `municipios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `niveles`
--

DROP TABLE IF EXISTS `niveles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `niveles` (
  `cve_nivel` int(11) NOT NULL AUTO_INCREMENT,
  `nivel` varchar(50) NOT NULL,
  PRIMARY KEY (`cve_nivel`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `niveles`
--

LOCK TABLES `niveles` WRITE;
/*!40000 ALTER TABLE `niveles` DISABLE KEYS */;
INSERT INTO `niveles` VALUES
(1,'Preescolar'),
(2,'Primaria'),
(3,'Secundaria'),
(4,'Bachillerato'),
(5,'Licenciatura'),
(6,'Maestría'),
(7,'Doctorado'),
(8,'curso'),
(9,'BBBBBBBBBBBBBBBBBBBBBBBB');
/*!40000 ALTER TABLE `niveles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `solicitud_turno`
--

DROP TABLE IF EXISTS `solicitud_turno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `solicitud_turno` (
  `id_solicitud` int(11) NOT NULL AUTO_INCREMENT,
  `curp` char(18) NOT NULL,
  `cve_mun` int(11) NOT NULL,
  `cve_nivel` int(11) NOT NULL,
  `id_asunto` int(11) NOT NULL,
  `id_estatus` int(11) NOT NULL DEFAULT 1,
  `telefono` varchar(20) DEFAULT NULL,
  `celular` varchar(20) DEFAULT NULL,
  `correo` varchar(100) DEFAULT NULL,
  `fecha_registro` timestamp NULL DEFAULT current_timestamp(),
  `turno_municipio` int(11) NOT NULL,
  PRIMARY KEY (`id_solicitud`),
  KEY `curp` (`curp`),
  KEY `cve_mun` (`cve_mun`),
  KEY `cve_nivel` (`cve_nivel`),
  KEY `id_asunto` (`id_asunto`),
  KEY `id_estatus` (`id_estatus`),
  CONSTRAINT `solicitud_turno_ibfk_1` FOREIGN KEY (`curp`) REFERENCES `alumno` (`curp`),
  CONSTRAINT `solicitud_turno_ibfk_2` FOREIGN KEY (`cve_mun`) REFERENCES `municipios` (`cve_mun`),
  CONSTRAINT `solicitud_turno_ibfk_3` FOREIGN KEY (`cve_nivel`) REFERENCES `niveles` (`cve_nivel`),
  CONSTRAINT `solicitud_turno_ibfk_4` FOREIGN KEY (`id_asunto`) REFERENCES `asuntos` (`id_asunto`),
  CONSTRAINT `solicitud_turno_ibfk_5` FOREIGN KEY (`id_estatus`) REFERENCES `estatus` (`id_estatus`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `solicitud_turno`
--

LOCK TABLES `solicitud_turno` WRITE;
/*!40000 ALTER TABLE `solicitud_turno` DISABLE KEYS */;
INSERT INTO `solicitud_turno` VALUES
(5,'SAHC020128HNLNRCA1',27,5,1,1,'8441044850','8441044850','cecireicito_@hotmail.com','2025-04-27 21:12:47',1),
(6,'JZUU290913HQRQIH61',4,5,1,1,'900 962 1668','998 451 8758','prueba2_2@example.com','2025-04-27 21:54:05',1),
(7,'QSFN951216HBCBVD50',4,5,1,1,'8888888888','88888888','prueba3@example.com','2025-04-27 21:56:42',2),
(8,'JAZY201021MQTYAT16',4,2,2,1,'77777777','2222222222','prueba4@example.com','2025-04-27 21:57:34',3),
(9,'URHV030622HZSWPD27',8,7,1,1,'4444444444','4444444444','prueba5_5@example.com','2025-04-27 21:58:51',1),
(10,'DPWX250315HCLMMF30',4,4,1,1,'233 869 7010','835 021 4501','prueba6@example.com','2025-04-27 22:22:47',4),
(11,'WMDQ140227MMNUTX11',1,3,1,1,'888 149 9430','835 021 4501','prueba7-7@example.com','2025-04-27 22:28:31',1),
(12,'DBSK690807MTLJAP16',27,8,4,1,'800 229 5164','918 716 5627','prueba8@example.com','2025-04-28 05:55:53',2),
(13,'MFUL990818MPLISO84',39,9,6,1,'200 217 0434','647 711 3585','final@example.com','2025-04-28 06:33:29',1);
/*!40000 ALTER TABLE `solicitud_turno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `usuario` varchar(30) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario` (`usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES
(5,'Administrador','admin1','1234');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'ticket_turno'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2025-04-28  0:39:15
