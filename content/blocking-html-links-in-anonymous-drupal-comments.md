Title: Blocking html links in anonymous Drupal comments
Date: 2010-01-05 20:46
Author: Bryce
Tags: Drupal
Slug: blocking-html-links-in-anonymous-drupal-comments

Time for another update on the battle against spam.

[Mollom](http://mollom.com) has been great in fending off the large
amounts of spam on the other site I run [Freaky Tiki
Productions](http://freakytikiproductions.com). But I allow anonymous
comments to be posted so you know that is just a breeding ground for
spam comments. And last year for some reason a lot more html linked spam
comments were getting through... and to say that it was annoying would
be the biggest understatement of last year ( maybe even this year but
its too soon to tell).

So I decided it was time to change to that, but I wasn't sure how. I
didn't want to give up on the anonymous comments, but I had to stop
people from posting linked spam. But after some tinkering I found a
solution:

once logged into Drupal, and under the Administer-\> Site
Configuration-\> Input Formats.

1)Click Configure for Full HTML

1.A) Un-check the box to allow unauthenticated users access to Full HTML

2) Return to Input Formats (the link at the top of the picture works
well)

3) Set Filtered HTML to be the default

4) Under the Filtered HTML Edit tab

4.A) click on the Configure tab at the top

4.B) inside the “Allowed HTML tags” input box, remove "bracket a bracket"

And that is it. You have now disallowed anonymous users from using full
html when posting comments and also stopped them from creating html
links within said comments.

This has done wonders for me in cutting down comment spam. Next up, try to
figure out the same thing for the name used when posting comments. The war
continues!
