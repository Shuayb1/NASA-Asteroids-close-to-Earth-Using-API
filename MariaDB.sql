CREATE DATABASE IF NOT EXISTS nasa_test_sql;

USE nasa_test_sql;

DROP TABLE IF EXISTS `asteroid_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `asteroid_listing` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Expense_date` date NOT NULL,
  `Asteroid_Name` char(255) NOT NULL,
  `Distance` varchar (20) NOT NULL,

  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expenses`
--

LOCK TABLES `expenses` WRITE;
/*!40000 ALTER TABLE `expenses` DISABLE KEYS */;
INSERT INTO `asteroid_listing` VALUES (1,'"(2018 SP1)', '5856078.5km'),(2, '(2018 SQ2)', '7181889.5km'), (3, '(2018 SC3)', '2375382.25km'), (4, '(2008 UV91)', '64872620km'), (5, '(2016 UN5)','68982216km');
/*!40000 ALTER TABLE `expenses` ENABLE KEYS */;
UNLOCK TABLES;
