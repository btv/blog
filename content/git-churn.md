Title: Git Churn
Date: 2011-11-01 16:36
Author: Bryce
Tags: Git, Mercurial
Slug: git-churn

I’m still really on the fence regarding the flame war between Git and
Mercurial; they both have their strengths and weaknesses. (In case
you’re wondering, the reason I haven’t been forced to make a decision
yet is because \$WORK uses Perforce .) When I learn about one trick in
one of these tools, I try to see if that trick is possible in the other.
So far this search has been pretty limited, and both applications seem
to be equally capable.

My buddy [OJ](http://buffered.io/) pointed me out to a Mercurial
extension called
[churn](http://mercurial.selenic.com/wiki/ChurnExtension), which is a
pretty nifty tool. It allows you to quickly see who made how many
changes to either a particular file or an entire repo (emails removed to
avoid these people being spammed).

guido 1970354 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

jack.jansen 1665771 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

solipsis 1588311 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

georg 1331332 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

martin 1005541 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

benjamin 697038 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

thomas 460885 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

christian 445461 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

fdrake 437229 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

tools 418957 \*\*\*\*\*\*\*\*\*\*\*\*\*\*

After finding out about this cool little feature I decided to see if Git
had something similar. After a little digging around I came across this
thread on StackOverflow(2) which talked about the Git
[shortlog](http://man.he.net/man1/git-shortlog) command. Running this
command with the “-sne” argument (as given from the StackOverflow page)
on my Project Euler git repo returned these results:

129 Bryce Verdier

42 Bryce Verdier

4 Bryce

1 bryce

While there are mentions of the gitstats project, I didn’t want to bring
that into the equation. I just want to compare the core applications.
Using a third party application, like gitstats, wouldn’t be fair to
Mercurial.

Seeing how both of these tools seemed to have similar capabilities, I
decided to investigate a little more. I started off by trying to see if
there might have been a flag to remove the stars from the Mercurial
churn output; while the stars are cool, I think the Git output looks
cleaner without them. Sadly, there isn’t a flag in churn to remove the
stars.

One thing I did like about churn over Git shortlog was the ability to
see either the number of lines changed or the number of change sets. I
think that having more options for how you want information presented is
a good thing. I also liked the output of churn over that of shortlog. I
want to see the user information before I see the number of changes they
made; I think it’s easier to process information that way than the other
way around. Sadly, even though there is a quite a lot of documentation
regarding formatting within the git log man page, there doesn’t seem to
be a print variable for summarizing one’s commits. Or for changing the
formatting if one uses the “-s” flag in the shortlog command.

As hard as I tried to break the tie between Git and Mercurial, these two
particular extensions each have their own advantages and disadvantages.
While it might be ideal to attempt to combine churn and shortlog into
the ULTIMATE CHANGE TRACKING EXTENSION, that is a task for another day
(and probably another programmer.) I guess the flame war between these
two tools is just going to have to continue for a little while longer.
