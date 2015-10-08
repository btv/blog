Title: First Flask web app
Date: 2012-11-28 21:54
Author: Bryce
Tags: Flask, Python
Slug: first-flask-web-app

As everyone should know by now, I love coding challenges. A while ago I
came across this one, which is rather long:

```
Using python with gevent 0.13.x and your choice of additional libraries and/or
frameworks, implement a single HTTP server with API endpoints that provide the
following functionalities:

$ curl -s 'http://127.0.0.1:8080/fib/13'
{"response": 233}

$ curl -s 'http://127.0.0.1:8080/fib/12'
{"response": 144}

$ curl -s 'http://127.0.0.1:8080/google-body'
{"response": "272cca559ffe719d20ac90adb9fc4e5716479e96"}

$ curl -d 'value=something' 'http://127.0.0.1:8080/store'
$ curl 'http://127.0.0.1:8080/store
'{"response": "something"}
```

At one point in my past a coworker talked about his love of the Flask
micro framework. Since this is just a simple web API, I figured I'd give
it a shot. This is a bit of a complicated task with many pieces, so
let's set a game plan for the rest of this post. I'm going to share the
specific functions related to each piece of functionality, then at the
very end I will share the entire code base so everyone can see how it
all fits together. One last note - to test out the run, you need to call
the run.py script, which will also be included below. Ready … BREAK!

Let's tackle the google-body endpoint first:

```python
@app.route('/google-body')
def google_body():
    try:
        sh = sha.new(urlopen('http://www.google.com').read())
        return jsonify({'response' : sh.hexdigest()})
    except Exception as e:
        return jsonify({'response' : 'ERROR: %s' % str(e)})
```

While this code block is very compact, it's not difficult to understand.
Go out to the internet, get the source code for google's home page and
insert that into the sha object. Wrap up the hexdigest results into a
dictionary object, throw that into the jsonify function, and send it on
its way. Don't forget to package it all in a nice try/except block for
safety.

Onto the Fibonacci API call:

```python
@app.route('/fib/<number>')
def fib(number):
    try:
        return jsonify({'response' : real_fib(int(number))})
    except ValueError:
        return jsonify({'response' : 'ERROR: Input not a number'})

@lru_cache()
def real_fib(n):
"""
This code was modified from the fib code in the python3 functools documentation.
"""
    if n < 2:
        return n
    return real_fib(n-1) + real_fib(n-2)
```

During PyCon US 2012, I became aware of the lru_cache decorator in
python3.3. I also learned that Raymond Hettinger wrote code that would
allow it work in
[python2](http://code.activestate.com/recipes/578078-py26-and-py30-backport-of-python-33s-lru-cache/?in=user-178123),
which allowed me to copy the code from the python3 documentation with
little modification. Knowing about the lru_cache allowed me to write a
nice and concise Fibonacci function reminiscent of something I might
write in Haskell or some other functional language.

Now the last part of this challenge, and the longest. Before we get to
the python, I feel that it might help your understanding if you know
what kind of database schema we're working with. So I'm going to post
that first, then the python code.

```sql
drop table if exists entries;
create table entries (
    id integer primary key autoincrement,
    value string not null
);
```

```python
@app.route('/store', methods=['GET', 'POST'])
def store():
    if request.method == 'POST':
        try:
            g.db.execute('insert into entries (value) values (?)',
                         [request.form['value']])
            g.db.commit()
            resp = jsonify()
            resp.status_code = 200
            return resp
        except Exception as e:
            return jsonify({"response" : "ERROR: %s" % str(e)})
    else:
        try:
            cur = g.db.execute('select value from entries order by id desc')
            #fetchone returns a list. To better meet the requirements,
            #just slicing the head of the list and output that.
            return jsonify({'response' : cur.fetchone()[0]})
        except IndexError:
            return jsonify({'response' : 'NOTHING IN THE DATABASE'})
```

This step is obviously a little more complex - the function has to
process both the GET and the POST HTTP methods, while using an outside
database to store and retrieve the information. I believe the code here
is simple enough for you to understand, so I won't explain every line.
For the POST method I had to do some juggling to get the desired return
results. In the example above a POST method works, but does not receive
an actual response. I was able to create this by using the jsonify
object to create an empty
[Flask.Response](http://flask.pocoo.org/docs/api/#flask.Response)
object, and then set the status code of that response.

At the end of the day I'm pretty happy with this. It wasn't a hard
challenge, but certainly allowed me to learn a bit about Flask. If I did
over again, I might improve things by creating my own decorator to
abstract all the try/except blocks. The errors would have to become more
generic and maybe less helpful, but that is a worthwhile cost for being
able to live the “Don't Repeat Yourself” mentality. The decorator would
look something like this (the code below has not been tested - caveat
emptor):

```python
def try_block(f):
    @wraps
    def wrapper(*args, **kwds):
        try:
            return f(*args,**kwds)
        except ValueError:
            return jsonify({'response' : 'ERROR: Input not a number'})
```

As more functions start to use this decorator it'll most likely get
uglier as it has to juggle more and more exceptions. While that is
certainly a cost of having all of the error checking wrapped up in one
location, the benefit that I can see is if another programmer were to
add a new piece of functionality, he would know exactly where to go to
add in the exceptions if it wasn't there already.

```python
@app.route('/fib/<number>')
@try_blockdef
fib(number):
    return jsonify({'response' : real_fib(int(number))})
```

I think this would clean up the function quite a bit.

Next time I'm going to show how to do this in Haskell using the Yesod
web framework. As always, questions, and comments are welcomed.


run.py

```python
from gevent.wsgi import WSGIServer
from playhaven import app, init_db
 
init_db()
http_server = WSGIServer(('0.0.0.0', 8080), app)
http_server.serve_forever()
```

challenge.py

```python
from __future__ import with_statement
from urllib2 import urlopen
from contextlib import closing
from flask import Flask, request, g, jsonify
from lru_cache import lru_cache
import sqlite3
import sha
 
DATABASE = '/tmp/challenge.db'
DEBUG = True
SECRET_KEY = 'c29tZXRoaW5nY2xldmVyaGVyZQ==\n'
USERNAME = 'challenge'
PASSWORD = 'chang3m3'
 
app = Flask(__name__)
app.config.from_object(__name__)
 
app.config.from_envvar('CHALLENGE_SETTINGS', silent=True)
 
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])
 
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()
 
@app.before_request
def before_request():
    g.db = connect_db()
 
@app.teardown_request
def teardown_request(exception):
    g.db.close()
 
@app.route('/fib/<number>')
def fib(number):
    try:
        return jsonify({'response' : real_fib(int(number))})
    except ValueError:
        return jsonify({'response' : 'ERROR: Input not a number'})
 
@lru_cache()
def real_fib(n):
    """
        This code was modified from the fib code in the python3 functools 
        documentation.
    """
    if n < 2:
        return n
    return real_fib(n-1) + real_fib(n-2)
 
@app.route('/google-body')
def google_body():
    try:
        sh = sha.new(urlopen('http://www.google.com').read())
        return jsonify({'response' : sh.hexdigest()})
    except Exception as e:
        return jsonify({'response' : 'ERROR: %s' % str(e)})
 
@app.route('/store', methods=['GET', 'POST'])
def store():
    if request.method == 'POST':
        try:
            g.db.execute('insert into entries (value) values (?)',
                         [request.form['value']])
            g.db.commit()
            resp = jsonify()
            resp.status_code = 200
            return resp
        except Exception as e:
            return jsonify({"response" : "ERROR: %s" % str(e)})
    else:
        try:
            cur = g.db.execute('select value from entries order by id desc')
            #fetchone returns a list. To better meet the requirements,
            #just slicing the head of the list and output that.
            return jsonify({'response' : cur.fetchone()[0]})
        except IndexError:
            return jsonify({'response' : 'NOTHING IN THE DATABASE'})
 
if __name__ == '__main__':
    app.run()
```
