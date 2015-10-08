Title: Google encypted searching
Date: 2010-06-03 03:02
Author: Bryce
Tags: encryption, Firefox, Google
Slug: google-encypted-searching


That [“series of
tubes”](http://www.youtube.com/watch?v=5ir_mKso_qc&feature=related)
known as the Internet went nuts two weeks ago because Google now allows
you to use their search engine through
[https](http://www.wired.com/threatlevel/2010/05/google-https-search/).
I consider this a good thing; the more traffic that flows around
encrypted the better. Yeah, there is some overhead to it, but everything
has a price and I feel the price is well worth paying.

</p>

Of course there are a slew of blogs out there telling Firefox users how
to use this feature. Saying pretty much the same thing: install a search
engine plugin (of which there are 10 on [Add-ons for
Firefox](https://addons.mozilla.org/en-US/firefox/search?q=google+secure&cat=4%2C0))
and you're good to go. But there is a small problem; I don’t use the
search box. I type my searches in the address field and the one plugin
that I did try didn’t change this - I was still searching unencrypted.
So like a good geek I went searching for an answer and found it. It's a
little preference called
[keyword.URL](http://kb.mozillazine.org/Keyword.URL)

All you have to do is:

-   (in a new window or tab) open up
    [about:config](http://kb.mozillazine.org/Firefox_:_FAQs_:_About:config_Entries)
-   Promise to be really careful ;)
-   Type “keyword” in the text field at the top and you’ll get back two
    entries:

    1.  keyword.URL
    2.  keyword.enabled

-   You’ll notice the default of keyword.URL as :
    `http://www.google.com/search?ie=UTF-8&oe=UTF-8&sourceid=navclient&gfns=1&q=`

    And we’ll just make a small change of adding an “s” to the end of
    http:

    `https://www.google.com/search?ie=UTF-8&oe=UTF-8&sourceid=navclient&gfns=1&q=`

-   verify that “keyword.enabled” is true, otherwise this little hack
    won’t work.

And that is all. Now the next time you use the address bar to search,
you to will be searching through https. One note though for
[vimperator](http://vimperator.org/vimperator) users - this trick
unfortunately doesn’t work (yeah, I’m bummed about that too). I’m not
sure why and I hope to figure that out next, but for now we’ll just have
to wait a little longer.
