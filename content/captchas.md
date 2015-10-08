Title: CAPTCHA's
Date: 2009-07-02 23:50
Author: Bryce
Tags: PERL, Drupal
Slug: captchas

Some of you might not know this, but I manage two different Drupal
sites. This blog (obviously ;) ) and the website for [Freaky Tiki
Productions](http://freakytikiproductions.com/). And for Freaky Tiki,
spam comments were quite a problem. The first way I tried to handle this
was to require all comments to be approved. Well, I'm pretty sure we
knew what happened with that. I wouldn't log in for months at a time,
and have handfuls of spam comments to delete, but also if someone put in
a legitimate comment, they would have to wait just as long to have it
posted. Not the best thing to do if you want people to continue posting
comments... damn you instant gratification.

So I decided I would use
[CAPTCHA's](http://en.wikipedia.org/wiki/Captcha) to help me out with
this. Grabbed the [Drupal's CAPTCHA
module](http://drupal.org/project/captcha) installed and configured it.
Now to be honest, I HATE CAPTCHA's. But at that moment I did not know of
any other alternative that would allow me to protect my site while also
not having to approve every comment. So I made a personal compromise to
use a text based CAPTCHA instead of the image-based one because I felt
that the text was less annoying. A couple of mouse clicks later, the
settings have been applied. And I had a nice warm fuzzy feeling inside.
I checked up on the site a couple of days later, and there was five or
six spammer comments on the site. I wasn't happy. So logged into the
site and deleted those comments. After doing that I took a quick moment
to find out how I could make sure it didn't happen again and that is
when Captain Obvious slapped me upside my head. I took a good look at
the test-based CAPTCHA (examples below):

What is the fifth word in the phrase "oqun oza edazoc qivu asic"?  

What is the second word in the phrase "yuyow ufif qugoto op ivasu
oxadewa"?

That slap hurt, but it caused me to realize that the format is very
static and thus easy to automate. And just to prove it I whipped up this
little kluge  

<link> in PERL:

<script src="http://bitbucket.org/btv/scripts/src/e421133b91d2/perl/text_captcha.pl?embed=t"></script>

Of course, text based CAPTCHA's weren't going to protect my site. So the
first thing I did was change to image based CAPTCHA's. My dislike of
them still exists, but as the better of two evils I accepted them...
what else could I do?

Days passed, the site is still comment spam clean (that I'm aware of
anyway), and I was talking to my good friend OJ, [who happens to write
his own blog](http://buffered.io), about my experience. And through the
natural progression of the conversation he shared his secret with me on
how he doesn't need CAPTCHA's on his site. For WordPress there are tools
to automate comment filtering. I wasn't aware that tools like this
existed. (Yeah, I should have thought about that, but I've never done
this before, so there is still a learning curve.) So it was only a
couple more clicks until I found these same tools for Drupal. And after
some research, I decided to use the [Mollom
module](http://drupal.org/project/mollom).

I'm not sure how well it'll work out. But for the price (free) it can't
hurt to try it.
