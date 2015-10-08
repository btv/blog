Title: Project Euler: Problem 10
Date: 2011-07-06 03:13
Author: Bryce
Tags: Haskell, Project Euler, Python
Slug: project-euler-problem-10

Thank you for your patience as you all (I'm sure) anxiously await my
next posting.

Not only has it been a really long time since I posted something
technical, it's also been a really long time since I posted a [Project
Euler](http://projecteuler.net/) solution. On that note, let's go over
the challenge:

```
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.  
```

Seems simple enough doesn't it? Let's find out. For Python the code is:

```python2
#!/usr/bin/python
"""
Python based code solution to problem 10 of project euler.
"""
import math

def is_prime(divided):
  divisor = 3
  sqrt_divided = int(math.sqrt(divided))
  while divisor <= sqrt_divided:
    if divided % divisor == 0:
      return False

    divisor += 2

  return True

if __name__ == "__main__":
  print sum([2] + [x for x in xrange(3,2000000+1, +2) if is_prime(x)])
```

And for Haskell the code looks like:

```haskell
module Main where

prime_wrapper:: Int -> [Int]
prime_wrapper divided = prime 3 divided (round . sqrt. fromIntegral $ divided)

prime:: Int -> Int -> Int -> [Int]
prime divisor divided sqrt_divided
  | divisor > sqrt_divided = [divided]
  | mod divided divisor == 0 = []
  | otherwise = next_prime
  where next_prime = prime (divisor + 2) divided sqrt_divided

main :: IO ()
main = print $ sum primes 
  where primes = 2 : [ x | x <- [3,5..2000000],  prime_wrapper x /= [] ]
```

I will be the first to admit that this problem is a little on the easy
side. Mostly because you can reuse the code you created for problems
[3](http://bryce.webfactional.com/project-euler-problem-3) and
[7](http://bryce.webfactional.com/project-euler-problem-7), or at least
I did. :)

Even though you and I know that Haskell will execute this code faster
than Python, I feel I still need to uphold the tradition of posting my
highly inaccurate execution times:

Python: 34.054s

Haskell: 20.690s
