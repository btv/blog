Title: Project Euler: Problem 6
Date: 2010-08-24 22:23
Author: Bryce
Tags: Haskell, Java, PERL, Project Euler, Python
Slug: project-euler-problem-6

After a nice vacation, the obsession continues.


```
The sum of the squares of the first ten natural numbers is,`

12 + 22 + ... + 102 = 385  

The square of the sum of the first ten natural numbers is,  

(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 385 = 2640. Find the
difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
```


Haskell:

```haskell
module Main where
 
main :: IO ()
main = do
       let x = [1..100]
       let sum2 = sum $ map (^2) x
       let sum1 = (sum x) ^2
       print (sum1 - sum2)
```

Python:

```python3
#!/usr/bin/python3
"""Project Euler solution using generators."""
 
sum1 = 0
sum2 = 0
 
for i in ((x,x ** 2) for x in range(1,100+1)):
    sum1 += i[0]
    sum2 += i[-1]
 
print(sum1 ** 2 - sum2)
```

PERL:

```perl
#!/usr/bin/perl
 
my $sum1 = 0;
my $sum2 = 0;
 
for (1..100)
{
  $sum1 += $_;
  $sum2 += $_ **2;
}
 
print ($sum1 **2 - $sum2);
```

Java:

```java
public class problem6
{
    public static void main( String[] args)
    {
      int sum1 = 0;
      int sum2 = 0;
 
      for( int i = 0; i < 100; i++)
      {
        sum1 += i;
        sum2 += i ^ 2;
      }
 
      System.out.println(sum1 ^ 2 - sum2);
    }
}
```

I admit writing a solution for Java is kind of a cheat. It's exactly the
same as the PERL solution, minus some language differences. But since I
started playing around with Android, I've started to spend more time
working with Java and it has just bled into this project.

</p>

### Run time comparison:

Because Java has to be compiled, I'm now using posting the time for the
compiled version of the Haskell solution.

Haskell: 0.004s

Python: 0.285s

Perl: 0.005s

Java: 0.625s

I'll refrain from insulting the speed of Java if you do. ;)

### Discussion:

Because of the simplicity of the solution, I tried to play around with
the answers between Haskell and Python. Originally my Python solution
looked more like my Haskell one, but after learning about generators I
decided I would use one for the Python solution. All in all I think it
would out rather well.

Questions, comments, insults?? (And not about me, about the code... I
know what you people are thinking!)
