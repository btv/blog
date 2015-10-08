Title: Using curl and a user agent string for web scraping
Date: 2009-11-18 04:11
Author: Bryce
Tags: Curl, PS3 Trophies
Slug: using-curl-and-a-user-agent-string-for-web-scraping

According to Wikipedia [web scraping](http://en.wikipedia.org/wiki/Web_scraping) is "is a computer
software technique of extracting information from websites." So let's
say you wanted to write a script to grab the number of trophies from
Sony's PS3 system. Web scraping might be a technique you might want to
consider. First move would be to use a web browser to get the URL to
eventually scrape:

"http://profiles.us.playstation.com/playstation/psn/profiles/L\_Cypher"
(yes, that is my ps3 user id and yes those are my stats)

Next step one would probably use a text browser to facilitate the web
scraping, like wget. So next step would be to put these two together and
see what happens:

```bash
wget http://profiles.us.playstation.com/playstation/psn/profiles/L_Cypher
```

But what is this:

```bash
wget <a href="http://profiles.us.playstation.com/playstation/psn/profiles/L_Cypher
--2009-11-17" title="http://profiles.us.playstation.com/playstation/psn/profiles/L_Cypher
--2009-11-17">http://profiles.us.playstation.com/playstation/psn/profiles/L_Cypher
--2...</a> 19:52:56--  <a href="http://profiles.us.playstation.com/playstation/psn/profiles/L_Cypher
Resolving" title="http://profiles.us.playstation.com/playstation/psn/profiles/L_Cypher
Resolving">http://profiles.us.playstation.com/playstation/psn/profiles/L_Cypher
Res...</a> profiles.us.playstation.com... 174.129.213.213
Connecting to profiles.us.playstation.com|174.129.213.213|:80... connected.
HTTP request sent, awaiting response... 403 Forbidden
2009-11-17 19:52:56 ERROR 403: Forbidden.
```

Let's see if this is what happens when we use curl (another website
grabber):

```bash
curl http://profiles.us.playstation.com/playstation/psn/profiles/L_Cypher
```

Now the response is even different than when using wget, but the most
important part is in the middle of the response ( shortened for
readability):

```html
<h2 align="center">Forbidden</h2>
<h4 align="center">Access is forbidden to this URL</h4>
```

So, now we see 3 inconsistencies here. With a "normal" web browser,
things work fine. Wget is down right rejected, and curl is reject but a
little more politely. At this point it looks like our web scraping
project would seem lost, but I don't give up that quickly. One thing
these three things have in common is a user agent. So if we can tell the
website we are a different user agent than what we really are, things
should work. Luckily enough for curl has this ability. And after a
little research we can now try new command to see if it works:

```bash
curl -A 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.4) Gecko/20091030 
Gentoo Firefox/3.5.4' 
http://profiles.us.playstation.com/playstation/psn/profiles/L_Cypher`
```

And VIOLA, we now get access to the site as if we were using firefox.
(html code not included for readability. If you wanna see the code you
can run it yourself.)

This is a good idea to keep in your mental toolbox, you never know when
you might need a trick like this in the future.

*Update (4/18/2010): A nice guy named John over at
[ps3inside.de](http://ps3inside.de) emailed me and told me that the link
above no longer works. I tested it myself and John is correct. It turns
out that Sony changed things up a little bit and now the trophies page
is all done in javascript. Being that javascript isn't html <duh> the
code above will **not** work.*
