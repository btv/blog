Title: Project Euler: Problem 5
Date: 2010-07-29 17:06
Author: Bryce
Tags: Haskell, PERL, Project Euler, Python
Slug: project-euler-problem-5

It's that time again. ;)

Question five reads:

```
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder. What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?
```

And here are my solutions (which I hope are correct this time).

Haskell:

```haskell
module Main where
 
import Data.List
 
divisible_11_to_20 number = 10 == (length $ unfoldr(\x -> if (snd $ quotRem number x) /= 0 || x < 11
  then Nothing
  else Just(x,x - 1)) 20)
 
-- solved this by the help on this URL:
-- (http)basildoncoder.com/blog/2008/06/10/project-euler-problem-5/
-- by increaing the loop from 2 to 2520, problem solves in seconds
main :: IO ()
main = print $ until (divisible_11_to_20) (+2520) 2520
```

As a quick note, yes I know that I could do this much quicker and
cleaner with a list comprehension. I decided to use unfoldr because I
wanted the experience of working with it. If it wasn't for this little
desire my answer would have looked a lot more like my Python answer.

Python:

```python
#!/usr/bin/python
 
def div_11_to_20(divided):
  return all([not bool(divided % x) for x in xrange(11,20+1)])
 
if __name__ == "__main__":
  count = 2520
  while div_11_to_20(count) == False:
    count += 2520
 
  print "%s" % count
```

And finally my Perl solution:

```perl
#!/usr/bin/perl
 
sub divide_11_to_20
{
  my ( $divided ) = @_;
 
  foreach (11..20)
  {
     return 0 if ($divided % $_);
  }
 
  return 1;
}
 
my $main_count = 2520;
while ( !divide_11_to_20($main_count) )
{
	$main_count += 2520;
}
 
print $main_count;
```

**Run Times:**

Haskell: 0m1.302s

Python: 0m0.769s

Perl: 0m0.223s

**Observations:**

It doesn't surprise me that the Perl solution ends up being the fastest
on these run times. I say this because per iteration the Perl solutions
has less calculations. Both the Haskell and Python solutions perform 10
divisions per iteration, where as the Perl solution only performs 10
divisions when the correct number is is being divided. Its one of those
things where the difference is very small, but will become larger as the
number of iterations increases.
