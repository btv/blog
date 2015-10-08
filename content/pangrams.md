Title: Pangrams
Date: 2011-12-29 17:30
Author: Bryce
Tags: Haskell
Slug: pangrams

![Photo]({attach}/images/96825282_b2548336c0.jpg)

If you haven’t figured it out by now, I enjoy solving problems. And over
the course of the last year or two, I’ve learned that interview
questions make for great problems to work on. Actual interview problems
are nice because they are usually quick, but have a quirk or two in
there that makes them challenging, unlike simple questions like the
[Fizz
Buzz](http://imranontech.com/2007/01/24/using-fizzbuzz-to-find-developers-who-grok-coding/)
problem that just checks if you have the most basic coding skills. (Has
anyone actually been asked that question in an interview?)

The most recent problem I got to sink my teeth into (found it on a
recruiting site, but not going to share where I got it; wouldn’t be fair
to the company posting the problem) is for finding pangrams in
sentences. If you don’t know what a pangram is
[Wikipedia](http://en.wikipedia.org/wiki/Pangram) defines them as, “a
sentence using every letter of the alphabet at least once.” Yeah, I
didn’t know what they were either until I started programming this
little puzzle. Here is the code:  

```haskell
module Main (main) where

import System (getArgs)
import qualified Data.Set as S
import qualified Data.Text as T
import qualified Data.Text.IO as TI (readFile)

buildList :: FilePath -> IO [T.Text]
buildList filename = TI.readFile filename >>=
    return . map (T.toLower . T.filter (/=' ')) . T.lines 

compareAndPrint :: S.Set Char -> String
compareAndPrint sset = if S.null result
                       then "NULL"
                       else S.toList result
  where result = S.difference (S.fromList ['a'..'z']) sset

main = do
  args <- getArgs
  sentences <- buildList $ head args
  mapM_  (putStrLn . compareAndPrint) $ map( S.fromList . T.unpack) sentences
```

I came up with the solution pretty quickly by using Sets. Having a set
of the alphabet and finding the difference of the letters used in the
sentence makes the problem almost trivial. The hard part for me was
figuring out how to filter out the spaces and change all characters to
lower case in the buildList function. I eventually figured it out, but
it took some head against wall action to get it right.

![Photo]({attach}/images/5271625268_2ae0f4b880.jpg)

This is going to be my last post for this year. I would like to wish you
all Happy Holidays and a Happy New Year. Thank for reading and see you
again in 2012. I would also like to thank everyone from
planet.haskell.org who decided to read this. Welcome!
