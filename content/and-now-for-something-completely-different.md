Title: And Now For Something Completely Different...
Date: 2010-09-14 03:52
Author: Bryce
Tags: Python
Slug: and-now-for-something-completely-different

Or maybe not. I came across this programming challenge through means I'm
not quite comfortable sharing on the interwebs. So disregard the origin
of this challenge, and just put those spare brain cells toward the
challenge and my answer.

**The challenge:**

```
Write a program that assigns products to sites in a way that maximizes the scores over
the set of customers. Each customer can only have one product and each
product can only be offered to one customer. Your program should run on the command
line and take as input two newline separated files, the first containing the
names of the product and the second containing the names of the customers. The output should
be the total SS and a matching between customers and products. You do not need to
worry about malformed input, but you should certainly handle both upper and lower
case names.
```

The algorithm for generating the number is as follows:

- If the length of the product name is even, the base score is the
number of vowels in the customer’s name multiplied by 1.5.

- If the length of the product name is odd, the base score is the number
of consonants in the customer’s name multiplied by 1.

- If the length of the product name shares any common factors (besides
1) with the length of the customer’s name, the score is increased by 50% above the
base score.

**My answer:**

```python
#!/usr/bin/python
 
import sys
from optparse import OptionParser
 
def build_list_from_file(filename):
    """
    builds a list from a newline delimited file.
    INPUT: string object, the filename
    OUTPUT: a list object with the lines of the file
    """
    temp_list = []
    try:
        with open(filename) as file:
            for lines in file:
                temp_list.append(lines.strip())
    except IOError:
        print "the file %s does not exist. Please look into it." % filename
        sys.exit(1)
 
    return temp_list
 
def count_vowels(name):
    """
    counts the number of vowels in a string.
    INPUT: string object, the string to be parsed
    OUTPUT: int object, the number of vowels in the string
    """
    vowels = 0
    for x in name.lower(): #setting all characters to lower case for comparison
        for y in ['a', 'e', 'i', 'o', 'u']:
            if x == y:
                vowels += 1
 
    return vowels
 
 
def count_consinants(name):
    return len(name) - count_vowels(name)
 
 
def generate_ss(matrix_object):
    """
    The function to generate the SS score based on the product name
    and customer name.
    INPUT: tuple object, with the name in the first element and 
           the product name in the second
    OUTPUT: a float object with the value after the computation
    """
    cust = matrix_object[0]
    prod = matrix_object[1]
    cust_factors = get_factors(cust)
    prod_factors = get_factors(prod)
    ss = 0.0
 
    if len(prod) % 2 == 0:
        ss = float(1.5 * count_vowels(cust))
    else:
        ss = float(count_consinants(cust)) # muliplicaton by 1 is implied.
 
    # by using sets, we can now use itersection to see if there are any
    # common factors between the two names
    if len(cust_factors.intersection(prod_factors)) > 0:
        ss *= 1.5
 
    return ss
 
 
def get_factors(name):
    """
    Retrive the factors of a particular number.
    INPUT: int object, number to gather factors of.
    OUTPUT: set object, the factors of a particular number
    """
    # using a variable instead of calling len() twice, should be faster
    top_num = len(name)
    return set([x for x in range(2,top_num+1) if top_num % x  == 0])
 
 
if __name__ == "__main__":
    """self explanitory... I hope."""
    parser = OptionParser()
    parser.add_option("-p", "--prod", dest="prod",
                      help = "Path to the prodcts file.Which should be newline delimited file.")
    parser.add_option("-c", "--cust", dest="cust",
                      help = "Path to the customer file.Which should be newline delimited file.")
 
    (options,args) = parser.parse_args()
 
    if not (options.prod and options.cust):
        print "A file for customers (-c) and one for products (-p) are needed."
        sys.exit(1)
 
    customer_list = build_list_from_file(options.cust) 
    prodcut_list = build_list_from_file(options.prod)
    matrix = []
    final_list = []
 
    matrix = [(a,b) for a in customer_list for b in prodcut_list]
 
    ss_list = map(generate_ss, matrix)
 
    # since we're zipping things up, might as well sort it
    # with largest SS value first
    zipped_by_ss = list(reversed(sorted(zip( ss_list, matrix))))
 
    # need to prime the list in order for this to work
    final_list.append(zipped_by_ss[0])
    del zipped_by_ss[0]
 
    while 1 < len(zipped_by_ss):
      j = 0
      while j < len(zipped_by_ss):
        if ( zipped_by_ss[j][1][0] is final_list[-1][1][0] or
             zipped_by_ss[j][1][0] is final_list[-1][1][1] or
             zipped_by_ss[j][1][1] is final_list[-1][1][0] or
             zipped_by_ss[j][1][1] is final_list[-1][1][1]
           ):
           del zipped_by_ss[j]
           continue
        j += 1
 
 
      final_list.append(zipped_by_ss[0])
      del zipped_by_ss[0]
 
    for item in final_list:
        print "%s has item %s, with SS score of %s." % (item[1][0], item[1][1],item[0])
```

**Thoughts about the code**

Before I posted this code here, I actually had the matrix generation
done with two for loops. Changing it to the list comprehension that is
in the code reduced the code size by a good eight lines or so, increased
the readability of that section of the program, and gave me a bit of a
speed up to boot. I will remember this little trick for the future.

When I was in school I took the requisite algorithms course, but that
was mostly about sorting and some other things. I don't recall them
going over a “duplicate removal” algorithm. For this part of the program
I believe my program runs correctly though I feel like it’s ugly code.
Doing the removal of duplicates with two indexes made sense to me for
removing the duplicates in line, but I feel like this could be optimized
more. I'm totally open to comments on all of my code, but I would really
appreciate it if people would focus more on that aspect of the program.
Also, if anyone knows of any “duplicate removal” style algorithms, or
places where I could learn more about them, I would be very grateful.
