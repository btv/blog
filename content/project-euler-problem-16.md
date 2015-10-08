Title: Project Euler: Problem 16
Date: 2012-10-25 16:12
Author: Bryce
Tags: Haskell, Project Euler, Python
Slug: project-euler-problem-16

I'm not dead yet! I've just been insanely busy the last month or two
with changing jobs and preparing my first programming presentation for
[BayPiggies](http://baypiggies.net) and [Silicon Valley Code
Camp](http://www.siliconvalley-codecamp.com/) (which is a post for the
near future). Both of these have kept me away from my blog. Let me make
it up to you with a solution to project Euler problem #16.

The challenge is:

```
2\^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
```

Let's start with some Python code:  

```python
#!/usr/bin/python
print sum([int(i) for i in str(2 ** 1000)])
```

For this solution, using a more functional approach definitely reduced
the code base. But one thing I was a little surprised about is that
having a list comprehension within the sum function is actually faster
than a generator expression. Usually one hears how generator expressions
are preferred over list comprehensions because they are more efficient
with memory, among other reasons. However, it's actually faster to give
sum a list. One quick caveat, this whole sum and list comprehension
thing applies to Python 2. The same seems to be also be true for Python
3, at least from the interpreter:  

```python3
>>> import timeit
>>> timeit.timeit("sum(int(x) for x in str(2 ** 1000))", number=1000)
0.11109958100132644
>>> timeit.timeit("sum([int(x) for x in str(2 ** 1000)])", number=1000)
0.09597363900684286
>>> timeit.timeit("sum(int(x) for x in str(2 ** 1000))", number=10000)
1.051396899012616
>>> timeit.timeit("sum([int(x) for x in str(2 ** 1000)])", number=10000)
0.9054670640034601
>>> timeit.timeit("sum(int(x) for x in str(2 ** 1000))", number=100000)
10.498383879996254
>>> timeit.timeit("sum([int(x) for x in str(2 ** 1000)])", number=100000)
8.992312036993098
```

On to the Haskell code:

```haskell
module Main where 
import Data.Char 

main :: IO ()
main = print . sum . map digitToInt . show $ 2 ^ 1000
```

Maybe it's just me and my Haskell/Python-centric brain, but I think the
algorithm is simple enough to easily see the similarities and
differences between the two languages. If I wanted to write the Haskell
code to better match the Python code (syntactic differences aside), it
would look like this: (inside the Haskell interpreter)

```haskell
Prelude Data.Char> print . sum $ [ digitToInt x | x <- show (2 ^ 1000)]
```

Even though this code may be easier to read for a Python programmer,
it's not “good” Haskell code. It'll get the job done, but the map is
obfuscated by the list comprehension. We can also adjust the Python code
to make it resemble Haskell by using map:

```python
print sum(map(int, str(2 ** 1000)))
```

But that might get you “dinged” because some people think that using map
is “too functional” or “not Pythonic”, even if the code might be faster.
I don't subscribe to that line of thinking...but that's a discussion for
another time.

Times:

python – list comprehension : .032s

python – map : .030s

haskell – list ( interpreted) : .155s

haskell – map (interpreted) : .155s

haskell – list (compiled) : .006s

haskell – map (compiled) : .006s

As always, questions, comments, and complaints are encouraged. I hope
everyone will forgive me for not posting for so long... sometimes life
happens.
