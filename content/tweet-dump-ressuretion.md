Title: Tweet Dump: Ressuretion
Date: 2011-02-23 18:12
Author: Bryce
Tags: CouchDB, Python, Twitter
Slug: tweet-dump-ressuretion

A long time ago I had a small series of blog entries talking about using
Python and MySQL to capture the Twitter public timeline. As I've hinted
at in my CouchDB post last year, I was going to bring this topic back
from the grave, this time using CouchDB instead of MySQL. After a lot of
reading and testing, I can now share the fruits of this labor.  

```python
import subprocess
import re
import sys
import couchdb
from couchdb.mapping import TextField, ListField
 
class Tweet(couchdb.Document):
    _id = TextField()
    _rev= TextField()
    tweet_data = ListField(TextField())

def get_tweets():
    final_texts = []
    command = """curl <a href="http://twitter.com/statuses/public_timeline.xml" title="http://twitter.com/statuses/public_timeline.xml">http://twitter.com/statuses/public_timeline.xml</a> | grep -A 3 '<status>' """
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (proc, error) = process.communicate()
    sys.stdout.flush()

    if error:
        print(error)
        sys.exit(1)

    ids = re.findall('[0-9]{10,13}', proc)
    texts = re.findall('<text>[\x20-\x7E]+</text>', proc)

    #check that the number of tweets ='s the number of ids
    # strip <text> fields from front & read
    if  len(ids) == len(texts):
        for i in texts:
            final_texts.append(i.rstrip('</text>').lstrip('<text>'))

        return(ids, final_texts)

    else:
        return (0,0)

if __name__ == "__main__":
    #using local couchdb server for now
    server = couchdb.client.Server()

    (ids, tweets) = get_tweets()

    if ids == 0 or tweets == 0:
        print("Mismatch on count between id's and tweets.")
        sys.exit(1)

    # Test to see if the db exists, create if it doesn't
    try:
        db = server['tweet_dumps']
    except couchdb.http.ResourceNotFound:
        db = server.create('tweet_dumps')

    for i in range(len(ids)):
        try:
            rev = db[ids[i]].rev
            db_tweets = db[ids[i]].values()[0]

            # to get rid of duplicate entries, which happen more
            # often than you think.
            if tweets[i] not in db_tweets:
                db_tweets.append(tweets[i])

            db.update([Tweet( _id = ids[i], _rev = rev,
                tweet_data = db_tweets)])

        except couchdb.http.ResourceNotFound:
            db.save(Tweet(_id = ids[i], tweet_data = [tweets[i]]))
```


To be frank, this started off as a copy and paste project. All the
CouchDB code was copied & pasted from the previous CouchDB post and the
tweet grabbing code was left over from one of the old tweet dump
scripts. Obviously some of the original code has changed as the Tweet
class is a little different, the database name is different, and one or
two other things have changed.

One of the things that really surprised me about doing this project now
as opposed to over a year ago was the amount of duplicates I captured.
The last time I did this, I didn’t get a single duplicate in the public
timeline. Now, in just one 24 hour capture I had one “tweeter” tweet the
same tweet 118 times. That is why there is code in there for not
appending duplicates (lines 69 and 70). I don't want to see the same
tweet 118 times, nor do I want to store it. I know space is cheap, but I
don't want to “pay” for keeping 118 copies of the same thing.

I will fully admit at this point that I found those 118 tweets by one
person just by doing a little mouse clicking through the CouchDB web
interface. I haven't yet figured out how to use the particular reduce
function to find which ID wrote the most tweets. That will more than
likely be the next blog post in this series.

After some time and reviewing the results of my capturing, I decided to
modify the code a little, this time including a time stamp for each
tweet captured (differences only pasted below):

```python
class Tweet(couchdb.Document):
    _id = TextField()
    _rev= TextField()
    tweet_data = DictField(Mapping.build(
        datetime = DateTimeField(),
        text = TextField()
    ))
 
...
 
 
    for i in range(len(ids)):
        try:
            rev = db[ids[i]].rev
            db_tweets_dict = db[ids[i]].values()[0]
            db_tweets_dict[str(datetime.datetime.now())] = tweets[i]
            db.update([Tweet( _id = ids[i], _rev = rev,
                tweet_data = db_tweets_dict)])
 
        except couchdb.http.ResourceNotFound:
            db.save(Tweet(_id = ids[i], tweet_data = {
                str(datetime.datetime.now()):tweets[i]}))
```

As you can see, there are some subtle differences between the two
scripts. One important difference is the shell out command was changed;
I used an extra grep to help reduce the data that python has to process.
I did this to reduce a lot of id & tweet mismatch counts I was getting.
This seemed to work so I stuck with it. The most important difference is
inside the Tweet class; the Tweet class was changed from a list of
TextFields to a DictField that houses a DateTimeField and a TextField.
The other serious difference is the code to update the tweet\_data
variable, as there’s different code used to update a list data type as
opposed to a dictionary data type.Otherwise these two scripts are
exactly the same.

This does lead me to question how Twitter views, perceives, or deals
with its public timeline. I alsowonder how accurate the portrayal of the
public timeline is in relation to Twitter usage. If the public timeline
is not an accurate portrayal of Twitter usage, then what is the point?
But if it is, then maybe people aren't using the service as much as
Twitter wants people to think they are.

--PS, sorry about the geshi putting in the html tag in the curl command
above. I'm trying to fix that right now.
