Title: De Morgan’s and (un)Pythonic code
Date: 2012-01-17 22:54
Author: Bryce
Tags: Python
Slug: de-morgans-and-unpythonic-code

![Photo]({attach}/images/5354727642_f678be9925.jpg)

The term “Pythonic” is a subjective and ambiguous one. There are plenty
of sites on the internet that try to explain what it means. Some of the
better sties will even tell you why one way of doing something is better
than another. I am adding my scrollingtext to the latter list.

I believe that one of the key requirements for writing pythonic code is
readability, as briefly mentioned in “The Zen of Python” by Tim Peters.
I also believe that this little poem (I use that term loosely here)
gives some pretty good hints on how to write pythonic code. (This is for
more of the thought process outside the general coding style stuff
defined in [PEP-8](http://www.python.org/dev/peps/pep-0008/)). Here is
the Zen of Python:

“Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

Flat is better than nested.

Sparse is better than dense.

Readability counts.

Special cases aren't special enough to break the rules.

Although practicality beats purity.

Errors should never pass silently.

Unless explicitly silenced.

In the face of ambiguity, refuse the temptation to guess.

There should be one-- and preferably only one --obvious way to do it.

Although that way may not be obvious at first unless you're Dutch.

Now is better than never.

Although never is often better than *right* now.

If the implementation is hard to explain, it's a bad idea.

If the implementation is easy to explain, it may be a good idea.

Namespaces are one honking great idea -- let's do more of those!”

Since this post is about pythonic code, I want to take a quick moment to
show you what I mean, saving you a google search or two in the process.
Here is a class method that I would consider non-pythonic code:

```python
def inNodeExistInPool(self, poolName, nodeName):
    try:
        currentNodes = self.__getNodesInPool(poolName)
        if currentNodes:
            for n in currentNodes:
        	if n == nodeName:
        	    return True
            return False
    except Exception, e:
        raise Exception('Exception in isNodeExistInPool: ' + poolName +
                        ', Node: ' + nodeName + ', Error: ' + str(e))
```

Now here is a more pythonic version of the same code:

```python
def isNodeExistInPool(self, poolName, nodeName):
    try:
        if nodeName in self.__getNodesInPool(poolName):
            return True
        else:
            return False
    except Exception, e:
        raise Exception('Exception in isNodeExistInPool: %s, Node: %s, Error: ' %
                       (poolName, nodeName, str(e)))
```

While the first version of the code above is not wrong and would
probably be the correct way to do this in other programming languages,
it’s not the best way to do it in python. (I also expect to see quite a
few comments on how other python programmers might improve the first or
second versions of these functions.)

Now that we have that little example out of the way, let me share with
you the motivation for this blog post. At work one day I saw some code
that looked like this:

```python
# ‘a’ being an instance of a class
if  not a.att1 and not a.att2 and not a.att3 and not a.att4:
    # more code down here
```

oddly enough, I remembered De Morgan’s Law from my formal logic courses,
so I used it to simplify the expression. Here is the proof (in formal
logic notation because it’s quicker):

-   ~P ^ ~Q ^ ~R ^ ~S
-   (~P ^ ~Q) ^ (~R ^ ~S)
-   ~(P v Q) ^ ~(R v S)
-   (~(P v Q) ^ ~(R v S))
-   ~((P v Q) v (R v S))
-   ~(P v Q v R v S)

After the logic juggling above I renamed the variables and then modified
the code to resemble the ending result:

```python
if not (a.att1 or a.att2 or a.att3 or a.att4):
    # still more code down here
```

After the change we can immediately see that I’ve reduced number of not
calls. While I’m sure there is some performance improvement, I seriously
doubt that it’s something that might be noticed by a human being, so
we’ll just discount this as any form of optimization. I believe I’ve
also made the code easier to read. The line itself is smaller, so a
maintainer would have less “things” to juggle in their head to verify
that the expression should pass or fail. Thus this code change has
fulfilled some of the ideas in the “Zen of Python,” particularly the
parts about “Simple is better than complex,” and “Readability counts.”
However, in the final product I’ve had to add some parentheses in order
for the logic to be correct, and this is where my ultimate question
lies. In a lot of “pythonic” code examples on the web, one doesn’t
really see “if” statements written like this one. So a somewhat
self-conscious part of me thinks that I even though I have gone through
the trouble of trying to make the code cleaner, I still haven’t gotten
the code to be “pythonic”.

After thinking about it a little more, I decided that my version is
pythonic. While I did add some clutter by adding parentheses, I also
removed 3 “not calls” and made the line easier to understand. I believe
this follows the spirit of pythonic code, even if it does not follow the
the code to the letter.

Top photo credit goes to: [mromtz](http://www.flickr.com/photos/mromtz/)
