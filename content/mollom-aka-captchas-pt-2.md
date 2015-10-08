Title: Mollom, aka CAPTCHA's pt 2
Date: 2009-07-20 21:36
Author: Bryce
Tags: Drupal
Slug: mollom-aka-captchas-pt-2

So a while ago I wrote about
[CAPTCHA's]({filename}/captchas.md). And I ended up saying
how I was going to try out [Mollom](http://mollom.com) for my automated
spam removal. Well, a couple of weeks later, I'm returning to this topic
to give some kind of review of Mollom.

So I have to say that right off the bat that it works, and it works
well. At the moment of this writing, not one piece of spam has infected
my comments. While at the same time, people created comments have gotten
through. And for all you out there wondering how Mollom can tell the
difference. And while that could be a whole blog post just to itself, we
can just shorten the idea down to a view simple concepts: [Bayesian
probability](http://en.wikipedia.org/wiki/Bayesian_spam_filtering) and a
very large sample set. We get an idea of how large of a sample set that
Mollom might have just by reading the a part of their front page (please
note that these numbers are dynamic and will change):

```
Mollom is currently protecting 10,310 active websites. The average
efficiency is 99.91%. This means that only 9 in 10,000 spam messages
were not caught. Mollom has caught 107,635,481 spam messages since it
started. Today we caught 179,461 spam messages. On average, 90% of all
messages are spam.
```

And doing some math with that statical model, you could probably come up
with a good sized grid of what are "good" words used in comments and
what are "bad" words used in spam.

One of the things I do like about Mollom, is within the Drupal module it
has a nice graph to let you know how much spam has been blocked and how
many legitimate operations have happened, as shown in the picture below:

IMAGE LOST

Some people might find this helpful, some might not. I do because it
gives me a metric towards how frequently my site is getting attacked by
spammers.

Some of you might be wondering about false positives. Mollom by default
sets up comments to be checked with the Mollom servers and if a comment
is flagged as potential spam, it requests the submitter to verify the
comment through an image based CAPTCHA. So while there is still a
CAPTCHA involved, its not the primary means of human authentication, so
I feel this is a healthy compromise.

The short of it is that if you happen to run a Drupal based site, and
want to avoid spam , I couldn't recommend Mollom enough.
