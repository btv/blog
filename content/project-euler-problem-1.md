Title: Project Euler: Problem 1
Date: 2010-06-18 03:39
Author: Bryce
Tags: Haskell, PERL, Project Euler, Python
Slug: project-euler-problem-1

So I'll admit it, I'm more than acceptably late to this party. OJ
started working on these problems years ago, while I was still coding
away on other stuff at school. Now that I'm not in school and needing a
challenge I'm doing the best I can to tackle the problems at Project
Euler. Since I'm also trying to pick up Haskell, this makes for a good
way to learn the language. This isn't my first time using a Functional
Programming language. But the last time I tried, it was forced upon me
at school with inadequate assistance and the whole experience left a bad
taste in my mouth. I'm glad that getting over the bad experience and
learning something new at the same time.

I've started keeping a github repo with my solutions for the various
problems. If anyone is interested in commenting on my code please do so.
I welcome all constructive criticism.

To start this thing off; problem one reads,

```
If we list all the natural numbers below 10 that are multiples of 3 or
5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum
of all the multiples of 3 or 5 below 1000.
```

Being this one was simple. I coded it up in Haskell, Python, and Perl.

Haskell:

```haskell
problem1 = sum $ filter (\x -> mod x 3 == 0 || mod x 5 == 0) [1..1000]
problem1' = sum $ filter (\x -> mod x 3 == 0 || mod x 5 == 0) [1..999]
```

Python:

```python
#!/usr/bin/python
 
def threeorfive(n):
  if ( n % 3 == 0 or n % 5 == 0):
    return True
  else:
    return False
 
def main():
  first_list = range(1,1000)
  second_list = filter(threeorfive, first_list)
  print "%s" % (sum(second_list))
 
if __name__ == "__main__":
  main()
```

Perl:

```perl
#!/usr/bin/perl
 
my $count = 0;
my $total = 0;
 
while ( $count < 1000)
{
  if ( $count % 3 == 0 or $count % 5 == 0)
  {
    $total += $count;
  }
 
  $count++;
}
 
print $total;
```

One thing that is nice about doing this in different languages, is that
you get to become aware of the differences between some of those
languages. For instance in Python the range function works a little
differently than I expected. I was expecting an inclusive range
function, one in which the 10 is included in the list. But that is now
how Python's range works. It gives me 10 numbers, starting with 1, the
end result is a list ending in 9. It's not a big deal and easily
fixable, but just not something I was expecting. That is why the Haskell
code has to functions in it. Just to verify that the Python code was
correct.

I'll be posting more answers as I complete them. So expect to see some
random posts with Euler solutions in them.
