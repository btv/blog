Title: Programming Praxis – Two Kaprekar Exercises
Date: 2011-03-23 19:57
Author: Bryce
Tags: Programming Praxis, Python
Slug: programming-praxis-two-kaprekar-exercises

Sorry I haven't written in a while. Been rather busy with life recently.
I'm still planning on continuing my Tweet Dump series, and I will post
that up soon. One of the reasons for the delay is because I'm learning
the [Colemak](http://colemak.com/) keyboard layout has slowed down my
typing quite a lot this week.

Anyway, yesterday's Programming Praxis question goes,

```
For today’s exercise we return to the world of recreational mathematics with 
two exercises due to the Indian mathematician Dattaraya Ramchandra Kaprekar. 
First we compute Kaprekar chains:

- 1. Choose any four-digit number, with at least two different digits.
Leading zeros are permitted.

- 2. Arrange the digits into two numbers, one with the digits sorted into
ascending order, the other with the digits sorted into descending order.

- 3. Subtract the smaller number from the larger number.

- 4. Repeat until the number is 6174. At that point, the process will cycle 
with 7641 − 1467 = 6174.

For instance, starting with 2011, the chain is 
2110 − 112 = 1998, 9981 − 1899 = 8082, 8820 − 288 = 8532, and 8532 − 2358 = 6174.

The second exercise determines if a number is a Kaprekar number, defined as an
n-digit number such that, when it is squared, the sum of the first n or n−1
digits and the last n digits is the original number. For instance, 703 is a
Kaprekar number because 7032 = 494209 and 494 + 209 = 703.
```

So here is the code I wrote and submitted to the comments section. I
will happily admit (like I did in my comment) that my isKaprekar
function is a modified version of one I saw in the comments
[here](http://programmingpraxis.com/2011/03/22/two-kaprekar-exercises/#comment-2711)
as it was cleaner than my first version and I wanted to try out the
"int(s[:-sz] or 0)" expression)

```python
#!/usr/bin/python3
import itertools

def isKaprekar(number):
    square = str(number ** 2)
    numlen = len(str(number))
    return number == int(square[:-numlen] or 0) + int(square[-numlen:])

def keprekar_chain(number):
    retlist = [number]
    if len(set(str(number))) > 2:
        while retlist[-1] != 6174:
            pers = [int(''.join(x)) for x in
                    itertools.permutations(str(retlist[-1]))]
            retlist.append(max(pers) - min(pers))
        return retlist
    else:
        return []

if __name__ == "__main__":
    print('Keprekar numbers from 1 to 1000:')
    print(*[x for x in range(1,1001) if isKaprekar(x)])
    print('Longest chain between 1000 and 9999')

    kep_list = []
    for x in range(1000,10000):
        tlist = keprekar_chain(x)
        kep_list.append((len(tlist), tlist))
        print(sorted(kep_list, key= lambda x: x[0], reverse=True)[0])
```

That's all for now; more to show up once I can type at normal speeds
again.
