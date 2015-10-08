Title: The Devil is in the Details
Date: 2011-04-28 20:40
Author: Bryce
Tags: Haskell
Slug: the-devil-is-in-the-details

This story happened a while ago, but because I've been so busy I haven't
really had the time to put it on (electronic) paper. While hanging out
on Twitter I saw a message asking why one version of Haskell code was
preferred over another. So I followed the link and saw the code below
(sorry for the formatting issues. Geshi isn't very good with http
links):

* 1) From
<http://learnyouahaskell.com/recursion#a-few-more-recursive-functions>

```haskell
take' :: (Num i, Ord i) => i -> [a] -> [a]
take' n _
| n <= 0 = []
take' _ [] = []
take' n (x:xs) = x : take' (n-1) xs
```

vs.

* 2) Just playin  


```haskell
take' :: (Num i, Ord i) => i -> [a] -> [a]
take' 0 _ = []
take' _ [] = []
take' n (x:xs) = x : take' (n-1) xs
```

Freefromz, the author of the code, was trying to do some code reduction.
And while his version does look a little nicer, the lack of error
checking makes the function a little incomplete and problematic. I
noticed this right away, but it took a little while to get the idea
across over Twitter; it's a bit difficult to relay complex concepts in
140 characters or less. Ultimately it was the tweet I sent him that
said, “@freeformz right. Let me ask you this question, in \#2 what
happens it I input -2 for n?” to which he replied, “@bryceverdier it
fails. duh on me. ;-)” that turned the light on for him.

This was my first time troubleshooting someone else's Haskell code. I'm
really grateful that it was an easy one, because if it was any more
complicated it probably would have been too difficult for my current
Haskell programming abilities--something I intend to work on improving
now that I have purchased my own copy of *Real World Haskell*. YAY!
