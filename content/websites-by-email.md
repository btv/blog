Title: Websites by Email
Date: 2010-05-20 23:29
Author: Bryce
Tags: PycURL, Python, SMTP
Slug: websites-by-email

I'd just like to share with you these forty-seven lines of python code
that amaze me. Not because they do anything special, but because they
represent something that is pretty important to programming languages,
modules, or libraries (depending on the language). Let's take a quick
gander at the code:

```python
#!/usr/bin/python
"""
#
# This is a simple script to grab the contents of a a website, 
# encoded into a MIME message, and email it
"""
import sys
import smtplib
import pycurl
from cStringIO import StringIO
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
 
data_buf = StringIO()
curl = pycurl.Curl()
 
# Setup pycurl to grab the data
curl.setopt(pycurl.URL, sys.argv[1])
curl.setopt(pycurl.WRITEFUNCTION, data_buf.write )
curl.perform()
curl.close()
 
# Begin creating email
#create html & text parts of the email
part1 = MIMEText(data_buf.getvalue(), 'html')
part2 = MIMEText(data_buf.getvalue(), 'text')
 
# next 5 lines put it all together
msg = MIMEMultipart('alternative')
msg['Subject'] = 'Website by Email'
 
msg.attach(part1)
msg.attach(part2)
 
# email away
# this code was copied from:
# http://www.mkyong.com/python/how-do-send-email-in-python-via-smtplib/
# Geshi keeps adding extra lines here, I'm not sure why
to = 'add_your_own'
gmail_user = 'add_your_own'
gmail_pwd = 'add_your_own'
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.login(gmail_user, gmail_pwd)
smtpserver.sendmail(gmail_user, to, msg.as_string())
print 'done!'
smtpserver.quit()
```

This little script started out as a work assignment (which I have
modified to make it more general). The task was to grab the contents of
a particular website and email them. Not terribly complicated, but also
not one I was thinking would be accomplished with twenty-eight lines of
actual code.

Let's take a second to review which modules are being used above:

The code used by PycURL to grab the website, and deposit the data into
the string.

StringIO module, to hold the contents of the website. (I wasn't able to
get a regular string to work here. If you know how, please tell me.)

The MIME module for reformatting the website contents.

The SMTPlib module, for having all the code in it to properly
communicate with a SMTP server, including TLS for encryption, to send
said email through the web.

It wasn't until doing this project that I fully realized the importance
of modules. It was these four modules that saved me uncountable hours of
coding, testing, and debugging. Even if I had written out the
functionality I needed from scratch, what I would have written would not
have anywhere near the functionality that these other modules provided.
In correlation to this, I wonder if there is some kind of connection
between how popular a lanugage is and how easily extendable it is. I
have no way to prove this of course, but both Perl & Python could be
good examples (and also happen to be the languages I'm most familiar
with). Both languages are popular, as shown by the normalized graph by
langpop.com, and both are also extremely easy to add extra functionality
to. The PycURL, CLyther, and PyCUDA modules are great cases in point.
PycURL allows Python to tap into the CURL library. CLyther allows Python
to use OpenCL, and PyCUDA allows Python to access the CUDA libraries. It
makes my head hurt just to think about the amount of code that it would
take to perform these same functions, if written from scratch.

After having this moment of realization, I find I am extremely grateful
to all the programmers out there who put in their time to help create
modules like these and to help them perform as well as they do. I tip my
hat at you all.
