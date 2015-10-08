Title: Project Euler: Problem 9
Date: 2011-01-06 23:37
Author: Bryce
Tags: Haskell, Project Euler, Python
Slug: project-euler-problem-9

Happy New Year Ladies(?) and Geeks

Trying to get the year off to a good start, I'm posting up my solution
for the ninth Project Euler problem. I'm not going to spend a lot of
time talking about it, because the solution is a pretty easy one. Here
is the code in Python:

```python3
#!/usr/bin/python3
"""
python solution for project euler problem #9.
"""

print( [a*b*(1000 - b -a) for a in range(1,500+1) for b in range(1,500+1) \
        if a * a + b * b == ((1000 -b -a) * (1000 - b - a))][0])
```

And here is the code in Haskell:

```haskell
module Main where
 
main :: IO()
main = print . head $ [a*b*(1000-b-a) | a <- [1..500] , b <- [1..500],
                       a ^ 2 + b ^ 2 == (1000 - b - a) ^ 2]
```

See, it really is that simple. There really isn't anything interesting
between to the solutions, but I would like to make a quick note on the
luxury of being able to use “head” in Haskell to simplify the whole
process. In the Python solution, the answer is generated twice, that's
just the nature of the algorithm, and to just get one number, I just ask
for the first item in the list. Thanks to Haskell's lazy evaluation, I
only have to calculate the answer once, and I think this may be
reflected in the run times.

So now the part that I know everyone loves to read the most, Times:

python-2.6.6 : .165s

python-3.1.2 : .110s

haskell(runghc) : 1.921s

haskell(compiled) : .086s
