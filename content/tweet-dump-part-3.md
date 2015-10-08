Title: Tweet Dump part 3
Date: 2009-12-21 23:06
Author: Bryce
Tags: Mysql, Python, Twitter
Slug: tweet-dump-part-3


Welcome back to another, and probably the last, instalment of the tweet
dump project.

The old tweet dump code was done locally. I wanted to see how things
would be affected if I ran the tweet dump code to a remote server. Just
to get an idea on how travel would affect latency.

So I changed things up a bit, I created a sql database through my
hosting provider and imported the schema into the remote database. At
which point I also modified up the tweet dump code to use this new
remote database. And after running the python script 5 times, here are
my numbers:

Run 1   43.998

Run 2   46.352

Run 3   45.029

Run 4   55.024

Run 5   49.174

Average 47.92


In my tweetdump code I have a lot of going back and forth between the
server and client;

```python
def getId(in_id):
	sql =  "select id from ids where twit_id = '" + in_id + "'"
	return runQuery(sql)
 
def addId(in_id):
	sql= "insert into ids values (null, '" + in_id + "')"
	runQuery(sql)
 
def addTweet(in_id, in_tweet):
	sql = "insert into tweets values ('" + in_id + "',\"" + in_tweet + "\")"
	runQuery(sql)
...
site_id = getId(ids[j])
if( not site_id):
    addId(ids[j])
    site_id = getId(ids[j])
```

When you see the three functions making up the code block near the
bottom, you might realize that there are three seperate sql calls to the
server. And while this might be fine for a local database, this is not
good for a remote one. So I decided to try my hand at creating a sql
function to reduce some of the back and forth between the two entities.

```sql
delimiter //
 
DROP FUNCTION IF EXISTS `get_set_ids`//
CREATE FUNCTION get_set_ids( in_tweet_id BIGINT )
RETURNS INT(10) UNSIGNED
BEGIN
DECLARE new_id INT(10) UNSIGNED;
SELECT id INTO new_id FROM ids WHERE twit_id = in_tweet_id;
IF ISNULL(new_id) THEN
     INSERT INTO ids VALUES (NULL, in_tweet_id);
     SELECT id INTO new_id FROM ids WHERE twit_id = in_tweet_id;
END IF;
RETURN new_id;
END //
 
delimiter ;
```

The function above takes the guess work away from the client, and keeps
it within the server. By doing this we avoid and entire round of
communication between the client & server. So in theory we should see at
least some kind of speed-up.

With the function above created I then went and modified the script to
take advantage of the function:

```python
def get_set_id(in_id):
	sql = "select get_set_ids(" + in_id + ")"
	return runQuery(sql)
...
site_id = get_set_id(ids[j])
addTweet(str(site_id[0][0]), final_texts[j])
```

After a bit of testing to make sure things worked, I ran five timed
tests (on the same hardware and from the same location, to try and
reduce any variables that might crop up).

Run 1   25.948

Run 2   24.35

Run 3   26.181

Run 4   24.667

Run 5   25.352

Average 25.3

The difference between the two averages is about 22 seconds. And to be
honest, I did not expect these changes to cut down my times by about
half. This was a little bit of a shock to me. I guess in this end this
is an example of how design can really matter.
