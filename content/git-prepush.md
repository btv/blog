Title: Git Prepush
Date: 2014-01-15 17:42
Author: Bryce
Tags: Git
Slug: git-prepush

I'm not sure how everyone else uses git, but at work we use it in a more
centralized manner, just like the subversion I migrated us from some
time ago. That means that for our changes we create a branch off of the
master branch, known as a "feature branch", make our changes, test said
changes, do a quick peer review, and finally merge back into master;
rinse; and repeat.

Since there are changes constantly going into the master branch, that
means we have to do what I call the git prepush shuffle, which is:

```text
checkout master  
update (pull) master branch  
checkout feature branch  
update (rebase) feature branch  
fix conflicts (if any)
```

Now the feature branch is ready to push for the review process then be
merged into master.

Why am I telling you all of this? Well, I hate having to type all of
that stuff out each and every time. One day I wondered if there was a
way I could improve this. I knew I could do aliases, so now it became a
question of if I could do more than one command within an alias. A
little internet searching lead me to this [StackOverflow
answer](http://stackoverflow.com/a/13125595), that showed that it was
possible.

This brought me to the next hurdle; I knew I needed to switch to the
master branch. But then how would I get back to the feature branch? A
little more rabbit hole falling got me to this [StackOverflow
answer](http://stackoverflow.com/a/7207542), which states that you can
go back to the previous branch with the "@{-1}" reference.

The one note I would also like to add before I show you what I did is
that I assume that:

```
[branch
    autosetuprebase = always
```

is set. WHich I've found really helpful when I'm working on a more
centralized manner which multiple committers.

My ultimate "creation" is this:

![Photo]({attach}/images/ItsAlive.jpg)

```
[alias]
    prepush = !git checkout master && git pull && git checkout @{-1} && git rebase master
```

So if anyone out there does the same dance that I do, feel free to use
this alias and save yourself some time and typing.
