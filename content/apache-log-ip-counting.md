Title: Apache Log IP Counting
Date: 2012-05-08 15:55
Author: Bryce
Tags: Bash, Haskell, Python
Slug: apache-log-ip-counting

It all started with a simple question: “Which single IP shows up the
most in an apache log file?” To which I ultimately came up with an
answer using a string of Bash commands:

```bash
less apache_log | cut -d '-' -f 1 | sort -r | uniq -c
```

This produced some text displaying how many times various IP addresses
made requests from an apache web server. After seeing the results and
thinking for a moment, I remembered that there is a “new” data type – as
of Python 2.7 and new to me at least – called
[“Counter”](http://docs.python.org/library/collections.html?highlight=counter#collections.Counter)
within the collections module in the standard library that would allow
me to recreate this in Python. So I quickly whipped up the code below:

```python
#!/usr/bin/env python
from sys import argvfrom collections
import Counter

if __name__ == "__main__":
    with open(argv[1]) as f:
        c = Counter(i.partition("-")[0] for i in f)
        for k,v in c.most_common():
            print '{:>4} {}'.format(v,k)
```

VIOLA! I get the same results as if I'd done it in Bash. Of course, like
the madman I am, I wasn't happy to just stop at Python; I had to write
this up in Haskell too. So I said “damn the torpedoes,” fired up my
favorite text editor, and started to hack and slash my way toward a
third version. After much documentation reading, internet searching, and
trial and error I can proudly proclaim, “MISSION ACCOMPLISHED”:

```haskell
module Main where

import System.Environment (getArgs)
import qualified Data.Text as T hiding (map, head, zip)
import qualified Data.Text.IO as TI (readFile)
import Data.Map hiding (map)

type Counter = (T.Text, Int)

mapUnpack :: Counter -> String
mapUnpack (k,v) = show v ++ " " ++ T.unpack k

sortMapByValue :: Map T.Text Int -> [Counter]
sortMapByValue = rqsort . toList

-- copied & modified by LYHGG in the recusion chapter
-- doing in reverse order as to better suit the output
rqsort :: [Counter] -> [Counter]
rqsort [] = []
rqsort ((k,v):xs) =
    let smallerSorted = rqsort [(k',v') | (k',v') <- xs, v' <= v]
        biggerSorted  = rqsort [(k',v') | (k',v') <- xs, v' > v]
    in biggerSorted ++ [(k,v)] ++ smallerSorted

main :: IO ()
main = do
    results <- getArgs >>= TI.readFile . head
    let results' = map (\x -> T.replace space nothing $ head $ T.splitOn dash x) $ T.lines results
    let results'' = fromListWith (+) . zip results' $ repeat (1 :: Int)
    mapM_ (print . mapUnpack) $ sortMapByValue results''
    where dash    = T.pack "-"
          space   = T.pack " "
          nothing = T.pack ""
```

The Haskell implementation took me longer than I expected as there were
a couple of challenges to figure out:

- 1) Learning the Data.Map datatype and figuring out how to build that
datatype from a list of IP addresses.  

- 2) Sorting the Map by value and not by key.  

- 3) Unpacking the Map to be printed.

The first problem was solved by a lucky internet search that showed me
an example of how to use the
['fromListWith'](http://www.haskell.org/ghc/docs/latest/html/libraries/containers/Data-Map.html#v:fromListWith)
function. This function performed the heavy lifting of sorting and
counting the IP addresses in the log file. For the sorting by value
instead of by key problem I was able to construct my own solution by
tweaking the quicksort example from *[Learn You a
Haskell](http://learnyouahaskell.com/recursion)*. The changes I made
expanded the tuple, allowing it to compare values and sort them in
descending order. For the text holding and manipulation involved in Map
unpacking, I've been told by other Haskellers that
[Data.Text](http://hackage.haskell.org/packages/archive/text/0.11.2.0/doc/html/Data-Text.html)
is “the way to go” (as the default String implementation is a little
slow and lacking features). While Data.Text did provide me an easy way
to split the string and grab the IP addresses, it also required
translating the IP addresses back into a String data type before Haskell
would print it. Thus my need for a specific function to create a string
based on each item in the Map. In the grand scheme of things having to
write the mapUnpack function wasn't horrible...it was just one more hoop
that I had to jump through before I could call this project complete.
After these modifications I was able to put this program together
without TOO much hassle, and in the end got the exact same results as
both the Bash string and the Python program.

Would I recommend writing these scripts for work instead of using the
string of Bash commands? No, especially if you're asked this question in
a high-stress situation. However, these little personal challenges were
a great way to expand my programming skills, particularly in learning
about new libraries like the collections module in Python and the
Data.Map module in Haskell. Having this random new knowledge might not
seem worthwhile upfront, but might come in handy in the future if I ever
encounter a problem that simple strings of Bash commands can't handle.
