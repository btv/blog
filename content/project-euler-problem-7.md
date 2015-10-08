Title: Project Euler: Problem 7
Date: 2010-10-06 01:10
Author: Bryce
Tags: Project Euler, Python
Slug: project-euler-problem-7

Here is the seventh installment of this series. And just to keep things
interesting I'm going to do something different this time around. I
still performed the solutions for Haskell, Java, and Perl (if you want
to view them check out my github repo), but instead of posting the code
for all four languages, I'm going to be talking about the evolution of
my Python solution, showing you all three revisions, and talking briefly
about how or why things changed.

Python code:

Solution 1:

```python3
#!/usr/bin/python3
 
import math
 
def is_prime(divided):
  divisor = 3
  sqrt_divided = math.sqrt(divided)
  while divisor <= sqrt_divided:
    if divided % divisor == 0:
      return False
 
    divisor += 2
  return True
 
if __name__ == "__main__":
  prime_list = [2]
  count = 3
 
  while len(prime_list) < 10001:
    if is_prime(count) == True:
      prime_list.append(count)
 
    count += 2
 
  print(prime_list[-1])
```

Looking at this first solution, we see that it follows the Haskell
solution quite closely. This is of course not an accident; I'm lazy. ;)
And since I'm still learning Haskell, I find it easier to learn the
basics of a language through translation. So this Python solution was my
first solution, which I then translated to Haskell.

Solution 2:

```python
#!/usr/bin/python3
 
import math
 
def is_prime(divided):
  divisor = 3
  sqrt_divided = math.sqrt(divided)
  while divisor <= sqrt_divided:
    if divided % divisor == 0:
      return False
 
    divisor += 2
  return True
 
 
if __name__ == "__main__":
  count = 1 #to substitute the prime number 2 in the example
  last = 0
  iterator = 3
 
  while count < 10001:
    if is_prime(iterator):
      count += 1
      last = iterator
 
    iterator += 2
 
  print(last)
```

So in coming up with my Java solution, I didn't want to deal with trying
to come up with a linked list-based solution for number storage. At
which point I had the great thought: why not just hold the last number
to be prime, and not all primes. Spending all this time with lists and
arrays instead of just straight Ints has really played with my thought
patterns. So after I wrote up the Java solution, I translated it to
Python, to see if there would be a reduction in the execution time based
on only using Ints instead of a list of Ints. Paint me a little
surprised when I saw that the difference was minimal if non-existent
most of the time.

Solution 3:

```python3
#!/usr/bin/python3
 
import math
 
def is_prime(divided):
  divisor = 3
  sqrt_divided = int(math.sqrt(divided))
  while divisor <= sqrt_divided:
    if divided % divisor == 0:
      return False
 
    divisor += 2
  return True
 
 
if __name__ == "__main__":
  # using a list to store each int value 
  data = [1,0,3]
 
  while data[0] < 10001:
    if is_prime(data[2]):
      data[0] += 1
      data[1] = data[2]
 
    data[2] += 2
 
  print(data[1])
```

After digging into how Python does its memory management, like Lists
being mutable while Ints are not, I modified the second solution so that
the Ints are now in a list. This way the Python memory manager does not
have to create a new variable to store each value. After these changes I
got the speed difference I was expecting to see between the first and
second revision.

Also, you might have noticed that in the is_prime function, I cast
math.sqrt to an Int. As math.sqrt returns a float, every time that
comparison happens for the while loop there has to be a conversion of
divisor from its current state of int to a float. Math.sqrt returns a
float, thus sqrt_divided is a float, and divisor is an int. So every
time that while loop cycles again, there has to be a conversion of an
int to a float. By casting that float to an int during the variable
declaration, I save myself a few thousand cast operations and shave off
a couple hundredths of a second from the total run time.

Language Run Times:

Python:

solution 1: .452s

solution 2: .433s

solution 3: .376

Haskell: .187s

Perl : .333s

Java: .128s

I don't think there are enough words in the English language to express
my surprise that Java actually had the lowest overall run time on this
one. I reran the Java solution a couple of times to see if it was an
error, but it's correct. This is something that I will have to dig into
more deeply to find out why.
