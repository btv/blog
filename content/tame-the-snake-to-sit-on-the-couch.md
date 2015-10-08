Title: Tame the Snake to Sit on the Couch
Date: 2010-11-24 17:52
Author: Bryce
Tags: CouchDB, Debian/Ubuntu, Python
Slug: tame-the-snake-to-sit-on-the-couch

A while ago I came across an aritcle that talked about using python with
couchdb. Since I'm interested in learning about the whole NoSQL movement
and am trying to understand where this new style of database server fits
in the schema (sorry, I couldn't resist) of things I decided to spend a
little time getting to know CouchDB better.

The system that I build this script on, tested with, and designed for is
Ubuntu (I'm running 10.10 if anyone cares to know). Although I installed
CouchDB through apt-get, I decided to get couchdb-python through
easy-install. I did this because the website documentation for
couchdb-python is written for the most recent version, and the apt-get
version is a little out of date.

So after you've installed Couchdb and couchdb-python you can now run the
script below:

```python
#!/usr/bin/python
'''
Simple script to start playing with the couchdb python package.
'''
 
import os
import subprocess
import re
import sys
import couchdb
from couchdb.mapping import TextField, ListField, DictField

class System(couchdb.Document):
    _id = TextField()
    _rev= TextField()
    uname = ListField(TextField())
    packages = DictField()

def get_packages():
    '''
    gather all of the packages on the system, and return a dictionary with
    the package name as the key, and the version as the value.
    '''
    process = subprocess.Popen("dpkg-query -W -f='${Package} ${Version}\n'",
                               stdout=subprocess.PIPE, shell=True)
    (proc, error) = process.communicate()
    sys.stdout.flush()

    if error:
        print(error)
        sys.exit(1)

    proc_dict = {}
    for x in proc.splitlines():
        m = re.search('(?P<package>\S+)\W(?P<version>\S+)', x)
        proc_dict[m.group('package')] = m.group('version')

    return proc_dict

def uname_list():
    ''' 
    Generate a list based on the data from uname, excluding the
    system's name.
    '''
    l = []
    l.append(os.uname()[0])
    for x in os.uname()[2:]:
        l.append(x)

    return l

if __name__ == "__main__":
    box_name = os.uname()[1]
    # When not using any arguments, defaults to localhost
    server = couchdb.client.Server()

    # Test to see if the db exists, create if it doesn't
    try:
        db = server['sys_info']
    except couchdb.http.ResourceNotFound:
        db = server.create('sys_info')

    # test to see if the computer already exists in the db
    try:
        rev = db[box_name].rev
        db.update([System( _id = box_name, _rev = rev, 
               uname = uname_list(), packages = get_packages())])
    except couchdb.http.ResourceNotFound:
        db.save(System(_id = box_name, uname = uname_list(), 
            packages = get_packages()))
```


If the script ran without errors then you should be able to this URL and
see your computers name as well a value of rev:1 – “some string of
characters”. If you click on your computer's name, you'll see all the
information the put inserted into the database. What you should see is
the “_id” field which will contain the computer's name. A “_rev” field
which will say the current revision number for this page. A list of all
the packages installed on the system... in no particular order. Finally
the output of uname, minus the computer name.

If the script did return some errors, what please make sure that you
have module initialization arugments correct (line 54). Couchdb-python
uses the defaults if there are no arguments, so in this case the module
is going to localhost for the host and the admin account, which has no
password. Yes, I know this is really unsafe but I'm just playing with
things right now.

One of the things I feel worth pointing out in the System class, in
order to create a ListField for CouchDB you must specify what the
ListField will contain. In this case (line 16) I am filling the
ListField with TextFields. Or in Python speak, filling the list with
strings.

I'm surprisingly fascinated with CouchDB... though I'm really hard
pressed to say why. At this moment I want to modify my tweet_dump
project to use CouchDB. So expect to see that series continued in a
little while.

One last thing, for those of you who celebrate it, Happy Thanksgiving!
