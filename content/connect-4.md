Title: Connect 4
Date: 2012-04-19 23:58
Author: Bryce
Tags: Python
Slug: connect-4

A couple of weeks ago I was lucky enough to have my employer send me to
PyCon. If you weren't at PyCon you missed out on a lot of things...like
the invading squirrel hordes. Thankfully, all of the talks are viewable
[here](http://pyvideo.org/category/17/pycon-us-2012). But PyCon is not
the focus of this post, just a starting point. At PyCon, in the vendor
area, there was the Thumbtack booth. The guys at this book weren't doing
the “normal” conference thing (passing out schwag to every being, living
or dead, that passed them); they actually made people work for their
swag. Thumbtack had a programming challenge that you had to submit a
solution to before they would give you either a large shot glass or a
glass beer stein.

The challenge was to accept a list of lists from standard input, and
parse it looking for a winner in a game of Connect 4. I believe this
could be a great interview question, and will be using it for the
upcoming interviews where I work. One of the reasons for this is that
it's deceptively difficult. While we as humans have been conditioned to
recognize patterns since birth, computers need to be taught every step
from the beginning. How do I go about teaching something that I don't
remember learning? But enough of my babbling - let's look at my
solution:

```python2
#!/usr/bin/env python

from __future__ import print_function
import sys

def char_check(row, col, char, prev_row=0, prev_col=0, count=0, direction=0):
    direction_dict = {1: None,
                      2: None,
                      3: None,
                      4: lambda: char_check(row, col - 1, char, row, col,
                                            count + 1, 4),
                      5: None,
                      6: lambda: char_check(row, col + 1, char, row, col,
                                            count + 1, 6),
                      7: lambda: char_check(row + 1, col - 1, char, row, col,
                                            count + 1, 7),
                      8: lambda: char_check(row + 1, col, char, row, col,
                                            count + 1, 8),
                      9: lambda: char_check(row + 1, col + 1, char, row, col,
                                            count + 1, 9)}

    if count == 3:
        print("Winner: %s" % char)
        sys.exit(0)

    direction_list = []
    direction_list_append = direction_list.append

    try:
        if (four_list[row][col - 1] == char and 
            (row != prev_row or (col - 1) != prev_col) and 
            direction in (0,4)): 
            direction_list_append(4)
        elif (four_list[row][col + 1] == char and 
              (row != prev_row or (col + 1) != prev_col) and
              direction in (0,6)):
              direction_list_append(6)
        elif (four_list[row + 1][col - 1] == char and 
              ((row + 1) != prev_row or (col - 1) != prev_col) and
              direction in (0,7)):
              direction_list_append(7)
        elif (four_list[row + 1][col] == char and
              ((row + 1) != prev_row or col != prev_col) and
              direction in (0,8)):
              direction_list_append(8)
        elif (four_list[row + 1][col + 1] == char and
              ((row + 1) != prev_row or (col + 1) != prev_col) and
              direction in (0,9)):
              direction_list_append(9)

        for d in direction_list:
            direction_dict[d]()

    except IndexError:
        pass

if __name__ == "__main__":
    try:
        four_list = eval(sys.stdin.read())
    except SyntaxError:
        print("Error getting list from the web, using preprogrammed backup.")
        four_list = [
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", ".", ".", ".", ".", "."],
                        [".", ".", "O", ".", ".", ".", "."],
                        [".", ".", "X", "O", "X", "X", "."],
                        [".", ".", "X", "X", "O", "O", "X"],
                        [".", ".", "O", "X", "X", "O", "X"]
                    ]
    finally:
        for r,_ in enumerate(four_list):
            [char_check(r, col, four_list[r][col]) for col,
                        _ in enumerate(four_list[r]) if four_list[r][col] != "."]

        print("No Winner")
```

Maybe it's my preference for functional programming coming out, but when
I looked at this problem I thought “recursion,” remembering from college
how much easier it is to solve the [Tower of
Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi) problem with
recursion than without. The problem became a little more complicated
when I went from solving the original example to generating and testing
a different board.

At the moment I'm trying to figure out a Haskell version of this
solution. Hopefully I'll have one soon and I'll update this page when I
do.

Before I posted this, I wrote a quick email to the person I spoke to at
the Thumbtack booth and sent him my solution. He thanked me for the
solution and requested my address to mail a mug to me, which showed up
in the mail couple of days ago. (Below is a pic of the mug filled with a
beautiful amber beer.) He also sent me a link to the company's blog post
about their experiences using a coding challenge to earn schwag. Here is
the
[link](http://www.thumbtack.com/engineering/how-we-got-people-to-earn-our-schwag/).
There are also some pretty impressive solutions to the challenge there,
including one done in regular expressions, which deserves a tip of the
hat in my book.

![Photo]({attach}/images/IMG_20120419_161121.jpg)
