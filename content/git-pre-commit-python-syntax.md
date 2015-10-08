Title: Git Pre-Commit Python Syntax
Date: 2011-09-08 15:47
Author: Bryce
Tags: Git, Python
Slug: git-pre-commit-python-syntax

All of us programmers have made this mistake before: we’ve submitted
code that we thought was correct only to have it fail during compilation
because of a simple syntax error. Just between you and me (and the rest
of the interwebs), I did this last week. Then I thought to myself that
it would be good to come up with a tool to help ensure it didn’t happen
again. I’m proud to say that on the Git front, I have fixed my problem.

Enter Git Hooks, a way to add scripts to various parts of the Git
workflow. Using what is called the pre-commit hook, I was able to write
up a quick bash script that goes through all the changed files in Git
staging area, check if they are Python files (based on the .py file
extension), and then run those Python files through Pylint to look for
various errors, including syntax and type errors.

So here is my git hook:

```bash
#!/bin/bash
 
files_modified=`git diff-index --name-only HEAD`
 
for f in $files_modified; do
    if [[ $f == *.py ]]; then
        pylint -E $f 
        if [ $? != 0 ]; then
            echo "Code fails pylint check."
            exit 1
        fi
    fi
done 
exit
```

Feel free to copy this and modify it for your own needs. My gift to you;
no charge. But an occasional “Thank you Bryce” email is always nice. I
also accept lavish gifts of cash or ThinkGeek merchandise.

One quick thing before I let you get back to your busy lives. If you
have an older version of Pylint than 0.24, the “-E” flag might need to
be changed to “-e”.
