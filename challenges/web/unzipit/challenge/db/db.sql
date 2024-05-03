DROP DATABASE IF EXISTS `ctf`;
CREATE DATABASE `ctf`;

USE `ctf`

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ;

INSERT INTO `users` VALUES (714587236485,'TEKUP_FTW','xlsdk0a7OAYieV4sadahlah0N');
