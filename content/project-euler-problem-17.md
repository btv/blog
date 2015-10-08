Title: Project Euler - Problem 17
Date: 2013-03-19 16:59
Author: Bryce
Tags: Project Euler, Python
Slug: project-euler-problem-17

It's been to long since I posted a solution to one of these challenges.
How time flies when you're having fun.

Here's the problem:

```
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?
```

Here is the python code:

```python2
#!/usr/bin/env python
ones = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
        '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': ''}
tens = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty',
        '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}
teens = {'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thriteen',
         '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen',
         '18': 'eighteen', '19': 'nineteen'}
hundreds = {0: 0, 1: "onehundredand", 2: "twohundredand",
            3: "threehundredand", 4: "fourhundredand",
            5: "fivehundredand", 6: "sixhundredand",
            7: "sevenhundredand", 8: "eighthundredand",
            9: "ninehundredand" }
if __name__ == "__main__":
    tot = 0
    for h in xrange(10):
        for y in xrange(1,100):
            try:
                t,o = tuple(str(y))
                if t is '1':
                    tot += len("{h}{t}".format(h=hundreds[h], t=teens[t + o]))
                else:
                    tot += len("{h}{t}{o}".format(h=hundreds[h], t=tens[t],
                                                  o=ones[o]))
            except ValueError:
                tot += len("{h}{o}".format(h=hundreds[h], o=ones[str(y)]))
    tot += len('onethousand')
    print tot
```

Even though I wrote it, I still look at it and think "that's not mine."
It's been a long time since I wrote a for loop within a for loop. There
isn't anything wrong with it, it's just not my style. This time however
I wasn't really able to come up with a solution that would allow me to
break out of the two for loops.

The one part of the code that I was surprised "worked" war breaking up
the digits by turning the number to a string then a tuple. This allowed
me to easily test an exception. This exception will only be thrown 10%
of the time. While exceptions might be expensive, the other 90% of the
time the code hums along without using a conditional. Everything has
costs, but I think that the cost of throwing an exception 10% of the
time as opposed to testing a conditional 100% of the time is a cost I'm
willing to accept.

I will admit that I did not code up another solution in a different
programming language. While part of that is due to being lazy - it's
good for the soul once and a while - I'm also not sure how I can code
this up in a functional language. I'm sure it can be done, I just don't
know how (If anyone has a link or idea please share it.) But because I
do like to compare things I tweaked the code to run within python 3.3.0.
The differences in time are so minimal that I'm not even going to post
it. If you're really inspired you can read the python 3 code
[here](https://github.com/btv/project_euler/blob/master/problem_17/python/problem17.py3).

Questions and comments welcomed. One quick side note to my readers: I'm
getting married this year (Yay!) and a lot of my free time is spent
juggling and planning. So I might not be blogging as frequently as
usual. Thanks for your patience.
