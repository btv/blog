Title: Project Euler: Problem 3
Date: 2010-07-02 06:09
Author: Bryce
Tags: Haskell, PERL, Project Euler, Python
Slug: project-euler-problem-3

OK, next installment of this. :)

The problem is stated as such:

```
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
```

Haskell:

```haskell
module Main where
 
factors count top_number
  | count >= top_number = []
  | zero_mod count = count : new_top: factors (count + 2) new_top
  | otherwise = factors (count + 2) top_number
  where new_top = round . fromIntegral $ top_number `div` count
 
zero_mod divisor
  | divide == 0 = True 
  | otherwise = False
  where divide = mod 600851475143 divisor
 
--prime :: Integer -> Integral -> Bool
prime divisor divided
  | divided == 1 = True
  | divisor >= sqrt_divided = True
  | mod divided divisor == 0 = False
  | otherwise = next_prime
  where next_prime = prime (divisor + 2) divided
        sqrt_divided = round . sqrt . fromIntegral $ divided
 
is_prime :: Integer -> Bool
is_prime input = prime 3 input
 
main :: IO ()
main = do
       let x = factors 3 600851475143
       let y = map is_prime x
       putStrLn $ show $ snd $  maximum ( zip y x)
```

Getting that sqrt function to work took me longer to figure out than I
want to admit. I was having the hardest time getting the numeric types
to play nice. I finally broke down and asked the haskell-beginners email
list to get the answer.

Python:

```python
#!/usr/bin/python
 
import math
 
top_number = 600851475143
 
def zero_mod(divisor):
  if top_number % divisor == 0:
    return True
  else:
    return False
 
def is_prime(divided):
  divisor = 3
  sqrt_divided = math.sqrt(divided)
  if divided == 1:
    return True
  else:
    while divisor <= sqrt_divided:
      if divided == divisor:
        return True
      elif divided % divisor == 0:
        return False
      else:
        divisor += 2
    return True
 
def main():
  count = 3
  go_to = top_number
 
  first_list =[]
 
  while count <= go_to:
    if zero_mod(count):
      first_list.append(count)
      go_to = top_number / count
      first_list.append(go_to)
 
    count += 2
 
  second_list = map(is_prime, first_list)
  print "%s" % max(zip(second_list, first_list))[-1] 
 
 
if __name__ == "__main__":
  main()
```

And finally Perl:

```perl
#!/usr/bin/perl
 
use strict;
use warnings;
 
my $top_number = 600851475143;
 
sub is_prime
{
  my ($divided) = @_;
  return 1 if ($divided == 1);
 
  my $divisor = 3;
  my $sqrt_divided = sqrt($divided);
 
  while($divisor <= $sqrt_divided)
  {
    return 0 unless ($divided % $divisor);
    $divisor += 2;
  }
 
  1;
}
 
my @f;
my $new_top = $top_number;
 
for(my $i = 3; $i <= $new_top; $i += 2)
{
  unless ($top_number % $i)
  {
    if (is_prime($i))
    {
      push @f, $i;
    }
  }
    $new_top = $top_number / $i;
}
 
print $f[-1];
```

Props goes out to zloyrusski who helped me figure out a major hang up
with Perl on this one. The for loop idea was his,though I really
diverted from his answer. Goes to show you how much two people really
can think differently. Hey Zloyrusski, is this Perl code looking better?
;) As always, I'm open to constructive criticism.

**--UPDATES--**

- 1) Code has been redone to fix the error talked about by agf. I find it
a little amusing that I still get the same answer though.  

- 2) I gotta start using less languages to do this in. If I make a
mistake I've gotta change & test three different versions.  

- 3) Times ( as requested by Caleb):

Haskell: 0.004s

Python: 0.205s

Perl : 0.136s

- 4) More props for zloyrusski for the division algorithm.
