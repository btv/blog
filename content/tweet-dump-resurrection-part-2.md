Title: Tweet Dump: Resurrection part 2
Date: 2011-04-14 17:21
Author: Bryce
Tags: CouchDB, Python, Twitter
Slug: tweet-dump-resurrection-part-2

I don't know about you, but when I hear or read the same thing three or
so times from random sources, I pay attention. And the pattern to each
of these comments have been about one thing: in the previous post in
this thread I did a shell out to curl from Twitter. Not only that, but I
used regular expressions for parsing xml. I won't deny it... I made some
pretty bad mistakes. The only consolation I have regarding these
mistakes is that I made them over a year and a half ago when I was just
starting to learn Python and not aware of just how many libraries the
standard install includes.

To help with the learning process, I'm going to show the original
version as well as the “fixed” version.

Original:

```python
def get_tweets():
    final_texts = []
    command = "curl http://twitter.com/statuses/public_timeline.xml | grep -A 3 '<status>' "
    process = subprocess.Popen(command, stdout=subprocess.PIPE, error=subprocess.PIPE, shell=True)
    (proc, error) = process.communicate()
    sys.stdout.flush()

    if error:
        print(error)
        sys.exit(1)

    ids = re.findall('[0-9]{10,13}', proc)
    texts = re.findall('<text>[\x20-\x7E]+</text>', proc)

    #check that the number of tweets ='s the number of ids
    # strip <text> fields from front & read
    if  len(ids) == len(texts):
        final_texts = [ i.rstrip('</text>').lstrip('<text>') for i in texts]

        return(ids, final_texts)

    else:
        return (0,0)
```

Fixed:
```python
def get_tweets():
    ids = []
    texts = []
    try:
        xmltree = xml.etree.ElementTree.parse(
        urllib.urlopen(
            'http://twitter.com/statuses/public_timeline.xml'
        ))
    except:
        return (0, 0)

    for x in xmltree.getiterator("status"):
        ids.append(x.find("id").text)
        texts.append(x.find("text").text)

    return (ids, texts)
```

For starters the changes I made were ditching the shell out to curl and
got the data from Twitter using the urllib library. Since I was grabbing
xml from Twitter, the output from the urllib.urlopen function could then
very easily be parsed and sorted by the xml.etree.ElementTree.parse
function. And since I had all the data in an xml object, I could very
easily get both the tweet text and the Twitter ID number.

I don't think I can stress enough how much cleaner the code is to read
in the fixed version. I feel that part of the cleanliness comes from
using the built-in libraries instead of trying to hack something
together. As an added bonus, since the code uses the Python built-in
libraries this code can now run on multiple platforms.

So there you have it, Internets. Once again I have wronged you by making
a mistake and have only now gotten around to understanding how horrible
of a mistake I made. Can you forgive me? Thank you.

For the super observant of you, one might notice that I also fixed a bug
from the original version of get_Tweets and the version from the last
thread. Happy Hunting.
