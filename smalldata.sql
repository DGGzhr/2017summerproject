-- MySQL dump 10.13  Distrib 5.5.57, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: smalldata
-- ------------------------------------------------------
-- Server version	5.5.57-0ubuntu0.14.04.1

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
-- Table structure for table `data`
--

DROP TABLE IF EXISTS `data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `data` (
  `domain` varchar(255) DEFAULT NULL,
  `value` varchar(255) DEFAULT NULL,
  `num` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data`
--

LOCK TABLES `data` WRITE;
/*!40000 ALTER TABLE `data` DISABLE KEYS */;
INSERT INTO `data` VALUES ('pressdisplay.com','1','1'),('v3club.net','0','1'),('theragonefamily.com','0','1'),('usnyk.com','0','1'),('pmdown.com','0','1'),('deepbluesoft.com','0','1'),('zeissimages.com','1','1'),('edsse.com','0','1'),('nttcomsecurity.com','1','1'),('install-stats.com','0','1'),('decoidc.com','0','2'),('deepbluesoft.com','0','2'),('movstube.com','0','2'),('arthalo.com','0','2'),('jsghsj.com','0','2'),('artisticpubs.com','0','2'),('artsuzhou.net','0','2'),('ashkaar.com','0','2'),('nripulse.com','1','2'),('mcfinley.com','1','2'),('registrydefenderplatinum.com','0','2'),('remastersys.com','1','2'),('worldsearchfirm.com','0','3'),('wotreplays.com','1','3'),('yangmei01.com','0','3'),('prontixintegration.com','0','3'),('prosoft-web.com','0','3'),('protekkimya.com','0','3'),('proteri.com','0','3'),('psmag.com','1','3'),('psychedelicme.com','0','3'),('janigoods.com','0','3'),('jasondwebb.com','0','3'),('clgw.net','0','4'),('click4corp.com','0','4'),('clinicalhematologyunit.com','0','4'),('mleb.com','0','4'),('mmimm.com','1','4'),('mmjbd.com','0','4'),('mmm-legal.com','0','4'),('mandyflores.com','1','4'),('manvel.net','0','4'),('maritz.com','1','4'),('vtopnet.cn','0','4'),('vwau.com','0','4'),('wabbc.com','0','4'),('fiberserver.com','1','5'),('filadelfiamedios.com','0','5'),('fileice.net','0','5'),('cbp.com','1','5'),('cc6c.net','0','5'),('ccgrad.com','0','5'),('nn5566.com','0','5'),('nnmwm.com','0','5'),('nocookie.com','1','5'),('nokiamoon.net','0','5'),('ttrcargo.com','0','5'),('tubs.com','1','5'),('tuco.com','1','5'),('aiai91.com','0','5'),('aidezy.com','0','5'),('aidigi.com','0','5'),('aidili.com','0','6'),('aihuay.com','0','6'),('ailantrip.com','0','6'),('aiminifans.cn','0','6'),('aint.com','1','6'),('opp168.net','0','6'),('oranum.com','1','6'),('orrorintugenensis.com','0','6'),('ortecrystal.cn','0','6'),('orzorestaurant.com','0','6'),('jessupbeautythailand.com','0','7'),('jeweleigh-handmade.com','0','7'),('jhbtyb.com','0','7'),('ollj.com','0','7'),('tmacconsulting.com','0','7'),('tngv.com','0','7'),('tntnm.com','0','7'),('today24news.com','1','7'),('toddrogers.com','0','7'),('nllv.com','0','7'),('nmalive.com','0','7'),('nmdd.net','0','7'),('abbmindoor.com','0','8'),('abierto365.net','0','8'),('abk50.com','0','8'),('plentyofcolour.com','1','8'),('pltk.com','0','8'),('pmdown.com','0','8'),('pmzk.com','0','8'),('pntq.com','0','8'),('pocketdentistry.com','0','8'),('policy-updatos.com','0','8'),('policyuncertainty.com','1','8'),('jqux.com','0','8'),('chriscartersounds.com','0','9'),('christophercountsstudio.com','0','9'),('chuangkit.com','1','9'),('chukumaandtunde.net','0','9'),('chungcudephanoi.com','0','9'),('cib.net','1','9'),('cidergame.com','0','9'),('cife.com','1','9'),('cila.cn','1','9'),('cilights.com','0','9'),('cirrohosting.com','0','9'),('kelbytraining.com','1','10'),('altman.net','1','10'),('alyssaprinting.com','0','10'),('amalacarpets.com','0','10'),('amanjana.com','0','10'),('amarillasinternet.com','1','10'),('sleepinginairports.net','1','10'),('slideworld.com','1','10'),('kenyawebexperts.com','1','10');
/*!40000 ALTER TABLE `data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-07-28  9:51:21
