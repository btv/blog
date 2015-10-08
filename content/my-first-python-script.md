Title: My First Python Script
Date: 2009-10-12 23:19
Author: Bryce
Tags: Python
Slug: my-first-python-script

I would like to introduce everyone to my first Python script. Just for
the sake of full disclosure it was originally put together by a coworker
and then passed off to me for completion. I haven't had much interest
until recently to even touch Python. I guess all of us should be so
lucky to have a job that forces us to grow in unexpected directions
every once and a while.

The script itself is nothing overly complicated, but I'm still proud of
it. The reason for that is because I had to dissect the language and
semantics to figure out what functionality was still needed to be added
to the script. As well as learn to read the language in order to work
with the parts that were existing before I touched it.

Just a quick overview of what it actually does ( or is at least suppose
to do ;) ). In a MySQL database somewhere in the world, there is a
database that holds a schema that was created to try and allow for
dynamic recreation of Apache virtualhosts config files at the push of a
button. (I'm being a little terse regarding things because I really
enjoy the project and have an upcoming blog post with more details. So I
don't want to spoil all the fun now. :) )

```python
# -*- coding: utf-8 -*-
import commands
import datetime
import unittest
import MySQLdb
import sys
 
###################### Constants #############################
 
# What user should we connect to the database as, for updating tables and such?
databaseUser = "******"
 
# What is the password to the database for the given user?
databasePassword = "******"
 
# What is the name of the database that we are connected to?
databaseName = "apache_config"
 
##################### Begin Code Implementation ###################
 
# Returns a set containing all tuples satisfying the given query.
def runQuery(query):
  db = MySQLdb.connect(user=databaseUser, passwd=databasePassword, db=databaseName)
  #db = MySQLdb.connect(host=host,user=databaseUser, passwd=databasePassword,
  #                     db=databaseName)

  # Execute the query and return the data.
  c = db.cursor()
  c.execute(query)
  return c.fetchall()
 
# Retrieves the master table that holds information on each of the virtualhosts
# currently being stored.
def retrieveMasterVirtualhostTable(in_virtualhost):
  return runQuery("select name, ipaddress from virtualhosts WHERE name = \"" +
                  in_virtualhost + "\"" )
 
#get all information for each virtualhosts based on virtualhost name
def retrieveSitesbyVirtualhosts(in_virtualhost):
  return runQuery("SELECT virtualhosts.name, virtualhosts.ipaddress, 
                   site.site_name, site.docroot, site.admin_email,
                   site.redirects, site.misc, site.site_id, site.misc 
                   FROM site,virtualhosts WHERE site.vhost_id = virtualhosts.id
                   AND virtualhosts.name= \"" + in_virtualhost + "\"")
 
# retrieve all aliaeses for a particular site
def retrieveAliasesbysite_id(in_aliases):
  return runQuery("SELECT alias_name FROM site_aliases WHERE site_id= " + in_aliases )
 
# Given a virtualhost entry, returns the header for the associated virtualhost.
def formatVirtualhostHeader(virtualhost):
  return 'NameVirtualHost ' + virtualhost[1] + 
         '\nLogFormat "%v %h %l %u %t \\\"%r\\\" %>s %b" vhost\n'
 
def convertWebsiteToVirtualhostEntry(site):
  if( not site[5] ):
      if ( site[4]): 
          ret= "\n<VirtualHost " + site[1] + ">\n" + \
                "	ServerAdmin " + "webmaster@" + site[2] + "\n" + \
                "	DocumentRoot " + site[3] + "\n" + \
                "	ServerName " + site[2] + "\n"
      else:
          ret= "\n<VirtualHost " + site[1] + ">\n" + \
                "	DocumentRoot " + site[3] + "\n" + \
                "	ServerName " + site[2] + "\n"
 
      # Add in site aliases.
      for alias in retrieveAliasesbysite_id(str(site[7])):
            ret += "	ServerAlias " + alias[0] + "\n"
 
      ret+=\
         "	ErrorLog /usr/local/var/apache/log/" + site[0] + ".error_log\n" + \
         "	CustomLog /usr/local/var/apache/log/" + site[0] + ".access_log vhost\n"
 
      if site[8]:
         ret += site[8] + "\n"
 
  else:
      ret= "\n<VirtualHost " + site[1] + ">\n" + \
            "	ServerName " + site[2] + "\n" 
 
      for alias in retrieveAliasesbysite_id(str(site[7])):
            ret += "	ServerAlias " + alias[0] + "\n"
 
      ret += "        Redirect " + site[5] + "\n"
 
  ret += "</Virtualhost>"      
  return ret
 
# Execution begins here.
def main():
 
  # grab information pertaining 
  virtualhost = retrieveMasterVirtualhostTable(sys.argv[1])
 
  # print the format stuff out at the top of the file
  print formatVirtualhostHeader(virtualhost[0])
 
  #now grab sites based on the virtualhost called
  virtualhostMaster = retrieveSitesbyVirtualhosts(virtualhost[0][0])
 
  # For each site in the virtualhostMaster "list"..
  for v in virtualhostMaster:
 
  ### Print entire output to the screen
    print convertWebsiteToVirtualhostEntry(v)
 
main()
```

I would just like to point out that although I'm proud of my work. I'm
not sharing this to try and receive praise from the internet. I'd
probably have better luck getting a STD from the internet than praise
for this little script. On the contrary, I'm posting this because I'm
new to Python, and I would like someone who has a little more experience
to guide me in the places that I might not have used the best python
methods to get things accomplished. For example, the line:  

```python
virtualhostMaster = retrieveSitesbyVirtualhosts(virtualhost[0][0])
```

Although this works, my intuition tells me that this isn't a very python
way of getting that data, using a double index like that. However I just
haven't been able to find the correct way to do this. So if someone out
there knows of a better way, I'm all eyes!
