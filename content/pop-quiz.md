Title: Pop Quiz
Date: 2009-08-26 20:01
Author: Bryce
Tags: PERL, VIM
Slug: pop-quiz

So, while at work you wrote some scripts. And after a code review your
boss tells you that he would like to see some variable names changed, to
help make the code more readable. So at the beginning of your code you
have:

```perl
#set script variables  

use vars qw/ %opts /;  

my \$append="\\@pdx\\.edu";

getopts( 'hrl:m:',\\%opts );

#make sure the arguments are provided, fail if \#not  

usage() if ( \$opts{h} || (!\$opts{m} || !\$opts{l}));

#everything's good, program can start now  

my $ldap= signin('true') || die;

#rename variables from opts to something more "readable"

my $username= $opts{l};

my $mail_alias= $opts{m};  

my $remove_flag= $opts{r};
```

But below this code section, $opts is being called quite a few times,
and the script is another 100 hundred lines of code or so. So what do
you do?

1)Tell your boss how adding these variables will reduce efficiency and
the overall speed of the code and revert the variables name.  

2)Do the changes manually  

3)open up vim or use sed with the expression
s/\$opts{<opts flag>}/\$<variable name>/g  

4)I don't care... but I do want to see what you think  

5)Other (Please leave a comment. How else will the rest of us learn?)

Answer:

Okay, this isn't the “only” answer, but it is what I did. Opened up VIM,
and used the following commands:

```
:32,$ s/$opts{l}/$username/g

:32,$ s/$opts{r}/$remove_flag/g

:32,$ s/$opts{m}/$mail_alias/g
```

For those of you not familiar with this let me explain. In the first
block of text, “:31,\$”, the “:” is just a way to signify to vim that
your going to preform a command. The “31,\$” is telling vim to limit the
following command between line 31 and the end of the file (which is what
\$ means). And then the second part s/\$opts{l}/\$username/g the command
itself. For those of you who are not familiar with sed syntax, it says
that your going to substitute an instance of $opts{l} for $username.
The ending g means to it more than once.

So when you put the whole command together you get, between line 31 and
the end of the file, replace all instances of $opts{l} with $username.

Hopefully this will help someone else as much as it helped me.
