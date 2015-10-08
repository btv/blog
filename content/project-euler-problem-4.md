Title: Project Euler: Problem 4
Date: 2010-07-08 17:19
Author: Bryce
Tags: Haskell, PERL, Project Euler, Python
Slug: project-euler-problem-4

If you been following me the last three times I've done this, then you
really don't need any introductions.

Problem four is as follows:

```
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit
numbers.
```

And my results in the usual three languages are:

Hasekell:

```haskell
module Main where
 
import Data.List
 
--Stole numberToList code from:
--http://www.rhinocerus.net/forum/lang-functional/95473-converting-number-list-haskell.html
numberToList = reverse . unfoldr (\x -> if x == 0 then Nothing else let (a,b) = x `quotRem` 10 in Just (b,a))
 
is_palimdrome number = num_list == reverse num_list
  where
    num_list = numberToList number
 
main :: IO ()
main = print . maximum . filter is_palimdrome $ zipWith (*) y z
  where y = [1000,999..100]
        z = [1000,999..100]
```

Python:

```python
#!/usr/bin/python
 
def int_to_list(number):
  return map(int, str(number))
 
def is_palindrome(number):
  local_list = int_to_list(number)
  return local_list == list(reversed(local_list))
 
if __name__ == "__main__":
  second_list = first_list = list(reversed(range(100,1000+1)))
  prod_set = map(lambda i,j: i*j, first_list, second_list)
 
  print "%s" % max(filter(is_palindrome,prod_set))
```

And finally, Perl:

```perl
#!/usr/bin/perl
 
use strict;
use warnings;
use List::MoreUtils qw(pairwise);
 
sub is_palimdrone
{
  my ($number) = @_;
 
  my @digits = split(//, $number);
  my @reversed_digits = reverse(@digits);
 
  for (my $i = 0; $i < @digits; $i++)
  {
    return 0 if $digits[$i] != $reversed_digits[$i];
  }
 
  return 1;
}
 
my @two = my @one = reverse((1..1000));
 
my @join = pairwise { $a * $b } @one, @two;
 
foreach(@join)
{
  if ( is_palimdrone($_))
  {
    print "$_\n";
    last;
  }
}
```

**Run Times**

Haskell: 0m0.034s

Python: 0m0.060s

Perl: 0m0.166s

For anyone that is not aware, haskell should win this statistic every
time. Out of the three languages its the only one that is compiled. If
anyone knows of a way to run haskell interpretively, and without using
ghci, please let me know. I've tried looking on the internets for this
piece of information, but have come up short.

I am still open to code suggestions or improvements. I have found these
to be very helpful and useful. So thank you to everyone that has said
something before.

**UPDATE**

So here is the new code that fixes the problem of my algo before. I'm
leaving the old up just to future readers aren't confused.

Thanks goes out to Jeremiah, Tom.B, Juster, and Guillaume for the code
ideas used to fix the mistakes in the code above. Thanks guys!

Haskell:

```haskell
module Main where
 
import Data.List
 
--Stole numberToList code from:
--http://www.rhinocerus.net/forum/lang-functional/95473-converting-number-list-haskell.html
numberToList = reverse . unfoldr (\x -> if x == 0 then Nothing else let (a,b) = x `quotRem` 10 in Just (b,a))
 
is_palimdrome number = num_list == reverse num_list
  where
    num_list = numberToList number
 
main :: IO ()
main = print . maximum $ [ x * y | x <- nums, y <- nums, is_palimdrome (x * y)] 
  where nums = [1000,999..100]
```

Python:

```python
#!/usr/bin/python
 
def int_to_list(number):
  return map(int, str(number))
 
def is_palindrome(number):
  local_list = int_to_list(number)
  return local_list == list(reversed(local_list))
 
if __name__ == "__main__":
  print "%s" % max([x * y for x in range(1000,100, -1) \
                          for  y  in range(1000,100,-1) \
                          if is_palindrome(x * y)])
```

Perl:

```perl
#!/usr/bin/perl
 
use strict;
use warnings;
use List::Util qw(max);
 
sub is_palimdrone
{
  my ($number) = @_;
 
  my @digits = split(//, $number);
  my @reversed_digits = reverse(@digits);
 
  for (my $i = 0; $i < @digits; $i++)
  {
    return 0 if $digits[$i] != $reversed_digits[$i];
  }
 
  return 1;
}
 
my @two = my @one = reverse((100..999));
my @three;
 
for my $one (@one)
{
  for my $two (@two)
  {
    my $three = $two * $one;
    next unless is_palimdrone($three);
    push @three, $three;
  }
}
 
print max(@three);
```
