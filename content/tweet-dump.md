Title: Tweet Dump
Date: 2009-10-20 04:56
Author: Bryce
Tags: Mysql, Python, Twitter
Slug: tweet-dump

So one day I was browsing the API of Twitter. And on this [particular
page](http://apiwiki.twitter.com/Things-Every-Developer-Should-Know#8AcommandlineisallyouneedtousetheTwitterAPInbsp)
on Twitter's website, they talked using a command line utility to
interact with Twitter. I was intrigued by this, so I decided to write up
a simple script to deposit the tweets and twitter ID's into a database.
Why? Because I could. ;)

So if for whatever reason you have to recreate my little experiment,
you'll need a couple of things:

- 1) A unix shell

- 1.1) grep

- 2) python installed and working

- 2.1) the mysqldb python module installed

- 3) mysql database installed

So here is my MySQL schema:

```sql
-- MySQL dump 10.11
--
-- Host: localhost    Database: twit_bank
-- ------------------------------------------------------
-- Server version	5.0.84-log
 
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
-- Table structure for table `ids`
--
 
DROP TABLE IF EXISTS `ids`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ids` (
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `twit_id` BIGINT(20) DEFAULT NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=50250 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
 
--
-- Table structure for table `tweets`
--
 
DROP TABLE IF EXISTS `tweets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tweets` (
  `ids` INT(10) UNSIGNED DEFAULT NULL,
  `tweet` CHAR(150) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;
 
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
 
-- Dump completed on 2009-10-19  0:22:26
```

And once you have that schema install, you can use the script below
(Obviously you'll need to change the username and password to your
particular database, but you don't need me to tell you that. My readers
are S-M-A-R-T!)

```python
#!/usr/bin/python
 
import os
import subprocess
import MySQLdb
import re
import sys
 
#variables
databaseUser = "*****"
databasePassword = "*****"
databaseName = "twit_bank"
 
 
def runQuery(query):
 
	db = MySQLdb.connect(user=databaseUser, passwd=databasePassword, db=databaseName)
	c = db.cursor()
	c.execute(query)
	db.commit()
 
	return c.fetchall()
 
def getId(in_id):
	sql =  "select id from ids where twit_id = '" + in_id + "'"
	return runQuery(sql)
 
def addId(in_id):
	sql= "insert into ids values (null, '" + in_id + "')"
	runQuery(sql)
 
def addTweet(in_id, in_tweet):
	sql = "insert into tweets values ('" + in_id + "',\"" + in_tweet + "\")"
	runQuery(sql)
 
def main():
 
	final_texts = list()
	j = 0
	site_id = list()
 
#code structure grabbed from: 
#http://buffis.com/2007/01/09/getting-output-of-a-system-call-in-python/comment-page-1/
 
        command = "curl <a href="http://twitter.com/statuses/public_timeline.xml" title="http://twitter.com/statuses/public_timeline.xml">http://twitter.com/statuses/public_timeline.xml</a> | grep -A 3 '<status>' "
	process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	os.waitpid(process.pid, 0)
	curl = process.stdout.read().strip()
	sys.stdout.flush()
 
	ids = re.findall("[0-9]{10,13}", curl)
	texts = re.findall("<text>[\x20-\x7E]{1,150}", curl)
 
	if ( len(ids) == len(texts)):
		for i in texts:
			temp = i.lstrip('<text>')
			final_texts.append(temp.rstrip('</text>'))
 
		while( j < 19):
			site_id = getId(ids[j])
			if( not site_id):
				addId(ids[j])
				site_id = getId(ids[j])
 
			addTweet(str(site_id[0][0]), final_texts[j])
			j = j + 1
 
main()
```

And this final last piece to put it all together, so you don't have to
do all the grabbing manually.(Don't forget to change the location of the
script.)

```bash
#!/bin/bash
 
while [ 1 ]
do
/home/bryce/programming/personal/scripts/python/twit2mysql.py
sleep 30
done
```

Now we get to the fun part. After about 24 hours of grabbing the public
timeline at 40 tweets a minute I got 50249 ID's and 50234 tweets on
record. Now while watching the numbers grow, there was a weird issue.
Most of the time there were more ID's than tweets. I'm not sure why this
is at the moment, but I'm curious enough to try and solve this bug.

Oh, and something that people should probably know. The reason why I'm
only grabbing 40 tweets a minute is because the first time I tried to
run this, I was grabbing more like 120 tweets a minute. And I was
blocked by Twitter for viewing the public timeline more than 150 times
in one hour. And I was blocked for the rest of the hour. So consider
that your warning.
