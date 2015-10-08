Title: The Devil is in the Details, part 2
Date: 2011-08-05 16:16
Author: Bryce
Tags: Haskell
Slug: the-devil-is-in-the-details-part-2

In the last blog post I made with this title, I told a little story on
how I helped a learning Haskell programmer see why his version of the
code wasn't as complete as the example given. I also thought that this
series wouldn't be having a second part to it, but it looks like I was
wrong.

I've recently been given a copy of “Learn You a Haskell For Great Good”
to write up a review for it. I've been trying to go through that book as
fast and thoroughly as I can because I really want to learn the material
and because I will be able to give a better review if I actually
complete the book. Yeah, big shocker there, I know.

Just a quick personal note before I continue. I'm not trying to point
out these short coming in code that I see to please my ego. I'm doing
this because I see a pattern that I don't think is correct and I don't
only want to prevent this problem from happening within my own code, but
also to bring the idea to public forefront so that other people can see
what is going on to and (hopefully) learn from it.

In “Learn You a Haskell”, more specifically Chapter 5 – High Order
Functions, the book walks someone through how to construct a Collatz
chain. The code in the book is:

```haskell
chain :: Integer -> [Integer]
chain 1 = [1]
chain n
    | even n = n : chain ( n ` div` 2)
    | odd n = n : chain ( n * 3 + 1)
```

and as an example from the book as well, when you run the above code you
get this as a result:

```haskell
ghci > chain 10
[10,5,16,8,4,2,1]
```

This is the right answer, but much like the code in the last blog post,
what happens if you give it a negative argument, let's say -10:

```haskell
ghci> chain (-10)
[-10,-5,-14,-7,-20,-10,-5,-14,-7,-20,-10,...]
#(I'm sure you can see the pattern at this point).
```

So I propose to make a small change to fix this problem. Here is my
version of chain:  

```haskell
chain :: Integer -> [Integer]
chain' 1 = [1]
chain' n
    | n <= 0 = []
    | even n = n : chain' (n `div` 2)
    | odd n = n : chain' ( n * 3 + 1)
```

At the end of the day, I'm just making the case that when I, or anyone
really, programs something up, a quick thought should be given towards
what type of input verification should be done before the
function/application/whatever runs so that it runs cleanly and
correctly. Ok, time to get off my soap box and start looking for these
same holes on the programs I've written.
