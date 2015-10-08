Title: Git Rollback
Date: 2011-07-21 04:39
Author: Bryce
Tags: Git, Mercurial
Slug: git-rollback

![Photo]({attach}/images/git_mercurial.jpg)

Lately I've been spending some of my free time giving back to the Python
community, sending in patches and doing patch reviews for the core
Python project. The Python project uses Mercurial for its source code
management. So I've been able to get a little more familiar with
Mercurial as of late. This led me to learn about the
[rollback](http://mercurial.selenic.com/wiki/Rollback) command, which
I've found to be helpful.

A while ago I was lucky enough to watch the live stream of the “Fringes
of Git” video by O'Rielly (which you can view
[here](http://bit.ly/dGYNPm?r=bb)). In the video I learned about Git's
[reflog](http://www.kernel.org/pub/software/scm/git/docs/git-reflog.html)
and how it keeps commits relative to the HEAD (or TIP for you hg users).
So I had the bright idea of trying to implement Mercuial's rollback
command by using an alias in Git.

For starters I put this alias into my .gitconfig file (avoid adding the
alias block if you already have one):

```bash
[alias]
    rollback = reset –hard HEAD@{1}
```

There... now you have the “git rollback” command.

Here was the process I used to test how similar the git version of
rollback is to the mercurial one:

- created two directories: test_hg and test_git

- ran hg init in test_hg and git init in test_git

- then just created a file called test.txt, added “test 1” into both
directories, then committed appropriately.

Repeated the process for “line 2” and “line 3” and committing the
additions.

This created a hg log like this:

```bash
changeset:   2:fddfdadb02cc
tag:         tip
user:        Bryce Verdier <bryce@scrollingtext.org>
date:        Tue May 10 11:06:30 2011 -0700
summary:     test 3 

changeset:   1:02ab8efc62
ceuser:      Bryce Verdier <bryce@scrollingtext.org>
date:        Tue May 10 11:06:22 2011 -0700
summary:     test 2

changeset:   0:ca1341dfc464
user:        Bryce Verdier <bryce@scrollingtext.org>
date:        Tue May 10 11:06:14 2011 -0700
summary:     test 1
```

and a git log like this:

```bash
commit 0357aa15e585692abda6e0c36213fce9f80523a4
Author: Bryce Verdier <bryce@scrollingtext.org>
Date:   Tue May 10 11:07:31 2011 -0700

    test 3

commit 7e2d21450b0e085ca57ac8e15b7f5b46314c1264
Author: Bryce Verdier <bryce@scrollingtext.org>
Date:   Tue May 10 11:07:24 2011 -0700

    test 2

commit d165a9825e96d40608b1da4319321c272424e019
Author: Bryce Verdier <bryce@scrollingtext.org>
Date:   Tue May 10 11:07:15 2011 -0700

    test 1
```

Next I ran “git rollback” and got a log like so:  

```
commit 7e2d21450b0e085ca57ac8e15b7f5b46314c1264
Author: Bryce Verdier <bryce@scrollingtext.org>
Date:   Tue May 10 11:07:24 2011 -0700

    test 2

commit d165a9825e96d40608b1da4319321c272424e019
Author: Bryce Verdier <bryce@scrollingtext.org>
Date:   Tue May 10 11:07:15 2011 -0700

    test 1
```

And when I did the same for mercurial, I got a similar result:

```
changeset:   1:02ab8efc62ce
tag:         tip
user:        Bryce Verdier <bryces@scrollingtext.org>
date:        Tue May 10 11:06:22 2011 -0700
summary:     test 2

changeset:   0:ca1341dfc464
user:        Bryce Verdier <bryce@scrollingtext.org>
date:        Tue May 10 11:06:14 2011 -0700
summary:     test 1
```

A difference showed up though when I ran the command a second time. When
I ran “git rollback” this was my log result:

```
commit 0357aa15e585692abda6e0c36213fce9f80523a4
Author: Bryce Verdier <bryce@scrollingtext.org>
Date:   Tue May 10 11:07:31 2011 -0700

    test 3

commit 7e2d21450b0e085ca57ac8e15b7f5b46314c1264
Author: Bryce Verdier <bryce@scrollingtext.org>
Date:   Tue May 10 11:07:24 2011 -0700

    test 2

commit d165a9825e96d40608b1da4319321c272424e019
Author: Bryce Verdier <bryce@scrollingtext.org>
Date:   Tue May 10 11:07:15 2011 -0700

    test 1
```

And when I ran “hg rollback” a second time I received an error:

```
no rollback information available
```

At this moment I'm not very knowledgeable in how Mercurial deals with
its logs. But at this cursory glance it appears as if the rollback
command completely removes all traces of the last commit. (Someone
please correct me if I'm wrong.) Also, the rollback does not go back any
further than one commit. I honestly think that this might be a good
thing because it could keep you from blindly shooting yourself in the
foot, if you need to go further back than one commit there is always the
[revert](http://mercurial.selenic.com/wiki/Revert) command.

While I don't know much about Git's internals either. However I can at
least make sense as to why the rollback alias functions this way. By
using the reflog to revert to the last commit, I end up undoing my
undue. Which can be seen when we review the reflog after running the
rollback command twice:  

```
0357aa1 HEAD@{0}: HEAD@{1}: updating HEAD7
e2d214 HEAD@{1}: HEAD@{1}: updating HEAD
0357aa1 HEAD@{2}: commit: test 3
7e2d214 HEAD@{3}: commit: test 2
d165a98 HEAD@{4}: commit (initial): test 1
```

This makes sense to me if I focus on two things in particular in the log
above. 1) Git's [SHA1 hashes](http://en.wikipedia.org/wiki/Sha1) in the
first column. And 2) looking at the log in reverse. Starting with the
last line, we see the first commit. And going up to the second to last
line we have the second commit. If you notice the hash values for
“commit: test 2” and “commit: test 3”, those are the same hashes used
for both of the git rollback commands, the second and first lines of the
log. So instead of removing an entry from the log, git is just moving
the head to the last commit.

While my alias isn't a complete copy of Mercurial's rollback command. I
do feel that the abstract idea behind it is still correct. And hopefully
I've done something to help make Git a little easier to use for someone
out there besides myself.
