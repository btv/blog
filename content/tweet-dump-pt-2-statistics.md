Title: Tweet Dump pt 2 : Statistics
Date: 2009-10-28 02:54
Author: Bryce
Tags: Mysql, Twitter
Slug: tweet-dump-pt-2-statistics

Some of you might remember my post last week titled [Tweet Dump]({filename}/tweet-dump.md).
And some of you might recall that I didn't include any statistics regarding my
findings. That was my bad, and I apologize. I'll do my best to not do that in
the future. So without taking up any more of your time let's get right to the
numbers.

So here is the SQL I used to check for the amount of ReTweets:  

```sql
select count(*) from tweets where tweet like '%RT%';
```

which returned:

1791 out of 50234, or 3.56%.

The SQL for tweets to at least one person:  

```sql
select count(*) from tweets where tweet like '%@%';
```

which returned:

20984 or 41.78%

The SQL for tweets with http links:

```sql
select count(*) from tweets where tweet like '%http://%';
```

returned:

9154 or 18.23%

This is the SQL I used to try and find any retweets:

```sql
select ids, count (*) as cnt from tweets group by ids having cnt > 1;
```

And sadly I get 0. Its a little weird that I can capture almost fifty
one thousand tweets and not one person tweeting more than once. I wanna
try again with this, but with a smaller window of time. Maybe people are
less likely to tweet more than once in a window. I don't know, I'm just
curious. Could something with my SQL. Anyone see anything wrong with it?

And finally the SQL for hashtags:

```sql
select count(*) from tweets where tweet like '%#%';
```

which returned 15117 or 30.09%

However, the SQL above also grabbed things like this:

"FACTのPVおちゃめで楽しい。これ見た後だと他"

Which are not incorrect per se. But I wasn't really wanting to include
characters from foreign languages in my search. Thus I'll need to come
up with a more defined SQL query that will parse tweets like this out of
my count.

Now some of you more detailed readers might have noticed that the
percentages only add up to 93.66%. The only meaning I could say to that
is maybe, just maybe, 6.34% is just regular tweets. Obviously, I'm not
doing a very in depth search, as there are probably tweets that will be
directed to someone and include a link. Which my numbers don't really
take into consideration. And if you really want to know these kinds of
numbers, ask a statistician. I'm a programmer. :P

Again, I'm not quite done with this project. But I thought I would take
the time to share my findings. I hope you found them as interesting as I
did.
