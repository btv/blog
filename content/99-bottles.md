Title: 99 bottles
Date: 2011-12-06 01:33
Author: Bryce
Tags: Programming Praxis, Python
Slug: 99-bottles

It’s been a while since I put up one of these simple code posts. Let me
fix that. :P

Quiet a while ago, this code needed to have the dust blown off of it.
Programming Praxis had its readers program out the song for
“Nintey-Nine Bottles of Beer on the Wall".

Here is my version of it:

```python
#!/usr/bin/env python

from __future__ import print_function

def output(in_int):
    if in_int != 1:
        return "%d bottles of beer on the wall, %d bottles of beer." \
                "You take one down, pass it around, %d bottles of beer" \
                "on the wall." % (in_int,in_int, in_int - 1)
    else:
        return "%d bottle of beer on the wall, %d bottle of beer." \
                "You take one down, pass it around, %d bottles of beer" \
                "on the wall." % (in_int,in_int, in_int - 1)

if __name__ == "__main__":
    [ print(output(x)) for x in reversed(xrange(1,99)) ]
```

That’s all there is to it really. The only enlightening thing about this
I can say is that this algorithm reminds me a lot of my [Code to
lyrics](http://scrollingtext.org/code-lyrics) post I wrote a little over
a year ago. It’s amazing how simple songs are when they’re broken down
to their basic elements. Anyone feel like setting up an “automatic song
generation” business with me?
