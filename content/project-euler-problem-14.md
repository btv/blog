Title: Project Euler: Problem 14
Date: 2012-07-25 16:45
Author: Bryce
Tags: Haskell, Project Euler, Python
Slug: project-euler-problem-14

```
The following iterative sequence is defined for the set of positive
integers: n → n/2 (n is even) n → 3n + 1 (n is odd).  Using the rule
above and starting with 13, we generate the following sequence: 13 → 40
→ 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1.  It can be seen that this sequence
(starting at 13 and finishing at 1) contains 10 terms.  Although it has
not been proved yet (Collatz Problem), it is thought that all starting
numbers finish at 1.  Which starting number, under one million, produces
the longest chain?  NOTE: Once the chain starts the terms are allowed to
go above one million.
```

Not many of you may be aware of this, but about a year ago I wrote up a
blog post that discussed Collatz chains in Haskell.  You can find that
post here: . Having some of the code already written made coming up with
the solution easier.  However, just because I had one function doesn't
mean I had the whole problem licked.  I still had a fair amount of work
in front of me.  Below is my code from the first attempt at a solution:

```haskell
module Main where
import Data.List

chain' :: Integer -> [Integer]
chain' 1 = [1]
chain' n
    | n <= 0 = []
    | even n = n : chain' (n `div` 2)
    | odd n = n : chain' (n * 3 + 1)

main :: IO ()
main = do
    let seqx = map chain' [3..1000000]
    let lengthx = map length seqx
    print . maximum $ zip lengthx seqx
```

This code appears to be logically correct but was incredibly slow - so
slow that after over 2 minutes it still hadn’t completed.  I admit I can
be a little impatient with these things from time to time, but in this
case something was obviously wrong.

I devised two optimizations:

*   Reverse the order of the list. I will be more likely to find the
    number with the longest chain near 1,000,000 than 3.
*   Use odd numbers only. This is based on the fact that in the chain'
    function an odd number gets multiplied right off the bat, whereas an
    even number is instantly divided by 2, and also on the assumption
    that a higher number will be more likely to have a longer chain.  (I
    admit this was a complete experiment - I had no proof that it would
    work ahead of time, and knew it gave me the right answer only after
    the fact.)

The code then morphed into:

```haskell
module Main where
import Data.List

chain' :: Integer -> [Integer]
chain' 1 = [1]
chain' n
    | n <= 0 = []
    | even n = n : chain' (n `div` 2)
    | odd n = n : chain' (n * 3 + 1)
    
main :: IO ()
main = do
    let seqx = map chain' [999999,999997..3]
    let lengthx = map length seqx
    print . maximum $ zip lengthx seqx
```

The problem I ran into with this code was that I received stack overflow
errors; my list of tuples holding another long list of int’s was taking
up to much memory.  I fixed this problem by computing the length of the
list immediately after generating it.  The new code looked like this:  

```haskell
import Data.List 
chain' :: Integer -> [Integer]
chain' 1 = [1]chain' n
   | n <= 0 = []
   | even n = n : chain' (n `div` 2)
   | odd n = n : chain' (n * 3 + 1)

main :: IO ()
main = do
    let seqx = map (\x → (x, length $ chain' x) [999999,999997..3]
    print . maximum $ seqx
```

This got me a result within the one minute time frame, but it still
wasn't the right answer.  Can you figure out why?  Using [the great code
Jedai posted in the comments of my Apache log
post](http://scrollingtext.org/apache-log-ip-counting#comment-384), I
was able to get my answer and finally complete the problem:

```haskell
module Main where

import Data.Tuple
import Data.List (sortBy)
import Data.Function (on)

chain' :: Integer -> [Integer]
chain' 1 = [1]
chain' n
    | n <= 0 = []
    | even n = n : chain' (n `div` 2)
    | odd n = n : chain' (n * 3 + 1)

main :: IO ()
main = do
    let seqx = map (\x -> (x, length $ chain' x)) [999999,999997..3]
    print . fst . head $ sortBy (flip compare `on` snd) seqx
```

![Photo]({attach}/images/bingo_computer_programming_languages.png)

After figuring that out, getting the python answer was a breeze:  

```python
#!/usr/bin/python
"""Python solution for Project Euler problem #14."""
 
from itertools import imap
 
def sequence(number):
    t_num = number
    count = 1

    while(t_num > 1):
        if t_num % 2 == 0:
            t_num /= 2
        else:
            t_num = (t_num * 3) + 1

        count += 1

    return (count, number)

if __name__ == "__main__":
  print max(imap(sequence, xrange(999999,3,-2)))
```

Here are the speed numbers:

Haskell (complied) : 14.758s

Python : 18.537s

Haskell (runghc): 15.217s

I think the use of recursion in my Haskell code is affecting its speed
of computation.  As I learned from problem 12, I can use the State Monad
again to speed things up.  But I also learned from the comments of
[problem 12](http://scrollingtext.org/project-euler-problem-12) that
some people were able to substitute a scan or fold in the State Monad’s
place.  So I decided to shoot for one more solution.  After studying up
on scan and fold, and finding that neither was really what I wanted, I
found iterate. Using iterate I was able to change the program to this:

```haskell
module Main where

import Data.Tuple
import Data.List (sortBy, iterate)
import Data.Function (on)

chain' :: Integer -> Int
chain' n  
    | n < 1 = 0
    | otherwise = 1 + (length $ (takeWhile ( > 1) $ iterate (\x -> if even x then x `div` 2 else x * 3 + 1) n))

main :: IO ()
main = do
    let seqx = map (\x -> (x, chain' x)) [999999,999997..3]
    print . fst . head $ sortBy (flip compare `on` snd) seqx
```

The new chain' function doesn't read as cleanly as the old one, but it
does remove the recursion I was talking about earlier.  The computer
gods rewarded my efforts by reducing the run times to these:

Haskell (complied) : 10.933s

Haskell (runghc): 11.744s

From 14.758 to 10.933 - almost 4 seconds taken off the clock!  I think a
speed up like that calls for some celebrating.  Which is exactly what
I'm going to do before I start on problem 15.
