Title: Mistakes
Date: 2009-10-05 17:57
Author: Bryce
Tags: Gentoo, VLC
Slug: mistakes

For a tech blog, I feel I write a lot of stories. And event though I
want to share what I've learned, I also feel that including a little bit
of background adds a nice layer of context to what information I'm
trying to pass along. I definitely don't wanna write a novel, but I feel
that a little backlog might add an extra element to what I'm trying to
convey.

Like this story: A couple of months ago I saw an article posted by
[HowToGeek](http://www.howtogeek.com/howto/2686/how-to-copy-a-dvd-with-vlc-1.0/)
on video recording in
[VLC](http://en.wikipedia.org/wiki/VLC_media_player<br%20/></p><p>).
After reading it I went home to try it out, and didn't get any luck, VLC
didn't record for me. At which point I commented on the blog saying as
much. (The date of my post is July 22, 2009 at 10:19 pm).

Here we are now, almost three months later and I have to eat those
words. VLC record does work in linux. But if your using Gentoo you need
to make sure you have the right USE variables set or else it won't
record.

I came across this while trying to figure out how to get x264 encoding
to work in ffmpeg. And in some random google link I came across this
[webpage](http://en.wikipedia.org/wiki/VLC_media_player) hosted on VLC's
website. It basically contained the “secret sauce” to build VLC properly
in Gentoo to get VLC to record. So of course I see and follow through
with the website of adding the line:

```
media-video/vlc wxwindows aac dts a52 ogg flac theora oggvorbis matroska
freetype bidi xv svga gnutls stream vlm httpd cdda vcd cdio live
```

to my /etc/portage/packages.use, then recompiled. And VIOLA, the record
button now functions properly. I admit to feeling a little sheepish for
posting my comment so quickly. And of course now I feel compelled to
post again to that article telling them I was wrong. Also, I feel like I
should also post a comment to the gentoo forums because I was not able
to find anything there regarding this problem, and hopefully I can help
someone out before it becomes a three month problem for them.

Internet, I learned my lesson. From now on I will do better due
diligence regarding my research before I post comments again. Can you
forgive me? Thanks!
