Title: Using curl and a user agent string for web scraping pt 2; Now with PHP
Date: 2009-12-01 20:46
Author: Bryce
Tags: Curl, PHP
Slug: using-curl-and-a-user-agent-string-for-web-scraping-pt-2-now-with-php

First off, Happy Thanksgiving to everyone, US readers especially. I know
I should have written this sooner, but the holiday kept me pretty busy
this year. And I hope you can accept my late well wishes.

And after you've had your fill of turkey, stuffing, and some pumpkin pie
maybe you got the chance to play around with what I posted [last week]({filename}/using-curl-and-a-user-agent-string-for-web-scraping.md).
And now lets build from that. Let's change the situation around a little
bit; and say that a command line utility isn't your thing for this
project. And you would like to use PHP.

First off, you'll want to make sure that your web server has curl
compiled in. And the easiest way is to use
[phpinfo()](http://php.net/manual/en/function.phpinfo.php) to find it,
and you'll want to look for this:

<center>
![Photo]({attach}/images/xampp-phpinfo.png)
</center>

If you see something similar to what I have above, your good. Otherwise
you'll either need to recompile your php to include libcurl, or complain
to your hosting provider. Afterwards we can accomplish what we want with
a couple lines of code:

```php
<?php
 $curl_options = array(
    CURLOPT_USERAGENT => "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.4) Gecko/20091030 Firefox/3.5.4",
    CURLOPT_RETURNTRANSFER => 1
 );

 $url= "http://profiles.us.playstation.com/playstation/psn/profiles/L_Cypher";

 $ch = curl_init($url);
 curl_setopt_array($ch,$curl_options);
 $content = curl_exec($ch);
 curl_close($ch);
?>
```
And now in your PHP code, you'll have a variable called \$content that
will contain all of the html code from the website. And how you wanna
parse information outside of that is up to you. Of course if anyone has
questions I will be happy to help out as best as I can.
