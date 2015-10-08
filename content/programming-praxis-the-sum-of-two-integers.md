Title: Programming Praxis: The Sum of Two Integers
Date: 2011-10-05 16:12
Author: Bryce
Tags: Haskell, Programming Praxis
Slug: programming-praxis-the-sum-of-two-integers

A couple of months ago the Programming Praxis website put up a challenge
to find a sum inside an array of integers (the direct wording of the
challenge can be found
[here](http://programmingpraxis.com/2011/07/19/sum-of-two-integers/))
and since I’ve come up with my own solution, this little challenge has
provided me with a lot of feedback.

Just to get some of the geeky stuff out of the way, here is the code I
wrote for the problem:

```haskell
import Data.List
import Data.Maybe
 
sumCheck :: Int -> [Int] -> [Int] -> Maybe (Int, Int)
sumCheck _ [] _ = Nothing
sumCheck total (x:xs) ys = if total' == Nothing 
                                then sumCheck total xs ys
                                else return (x, (ys !! ( fromJust total')))
                           where total' = (total - x) `elemIndex` ys
```

In thinking about the problem a little bit I came up with this
subtraction approach. My first approach was to use addition and add
every item in the array against all the other items. But this method
didn’t sit well with me. After a little bike ride I came up with the
code you see above.

After I wrote it, I submitted my code to the Haskell-beginners email
list asking for critiques and possible enhancements. Arlen Cuss
contributed a slight improvement of my code:

```haskell
sumCheck total (x:xs) ys =
let diff = total - x
    in  if diff `elem` ys
        then Just (x, diff)
        else sumCheck total xs ys
```

And Adityz Siram contributed his version. Which is basically the first
algorithm that I came up with and wanted to improve upon. His code is
here:

```haskell
sums i as bs = [(x,y) | x <- as, y <- bs, x + y == i]
```


Finally, Gary Klindt took all of our code snippets, used some
performance analysis tools inside GHC and came up with some run times
that are (hopefully) more accurate than running time on an application.
Here are those stats:

```haskell
print $ sumCheck 500 [1..1000] [1..1000]

sumCheck1: 58,648

sumCheck2: 58,484

sumCheck3: 70,016

print $ sumCheck 5000 [1..10000] [1..10000]

sumCheck1: 238,668

sumCheck2: 238,504

sumCheck3: 358,016
```

(unit: byte)

Out of the three code snippets, my function was in the middle,
speed-wise. But I think that it’s also really nice to see how much
better it is than the regular addition method. It’s also nice to see how
the little change made to my code can improve the overall speed of the
function.

At the end of the day I take a little bit of pride in myself for coming
up with an improved algorithm for this task on my own. I know that on a
hardware level, subtraction takes more time than addition. But I get the
improvements I get because I reduce the number of additions and
comparisons I have to make in order for the function to be complete. I
also estimate the worst case speed for my algorithm to be O(n), which
isn’t too shabby.

When I started learning Haskell, one of the things I read on the
internet was how the people who programmed it were helpful to one
another. I was skeptical when I first read that, but I have to say that
all of my doubt has been removed. And it is interactions like this that
make me glad to participate in a community as helpful as this one.
