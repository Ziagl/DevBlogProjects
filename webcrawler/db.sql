CREATE TABLE `links` (
  `link` varchar(255) NOT NULL,
  `id` int(10) unsigned NOT NULL auto_increment,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `link` (`link`)
) ENGINE=MyISAM CHARSET=utf8