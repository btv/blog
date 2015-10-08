Title: Interview question: Recreate groups
Date: 2010-02-05 02:49
Author: Bryce
Tags: PERL
Slug: interview-question-recreate-groups

I was in an interview and another interview walked in and said “Hi, do
you know the groups tool in unix?” At which point i said “Yes”. At which
point the interview hands me a whiteboard marker and says “Great. Write
it”. And after a couple of minutes of thinking about how to do it, I
wrote it down.

Now, I didn't end up doing it on a whiteboard, I did it on a piece of
paper I had, which I kept, but unfortunately I have not beed able to
scan it for everyone's reading enjoyment. But I'll do that in the
future.

So once I got home after the interview, I took the algorithm, and
applied proper PERL syntax. And here is the code:

```perl
#!/usr/bin/perl
#######################################################################
#	Created By: Bryce Verdier
#	on 1/19/10
#	Function: rework the output of the unix groups command
#	NOTE: FOR USE ON UNIX MACHINES!
#######################################################################	          
use warnings;
use strict;
use Getopt::Std;
 
our($opt_u);
getopts('u:');
 
#Get the results from /etc/groups
my $groups= `grep -w $opt_u /etc/group`;
 
#split it into an array for per line processing
my @split_groups= split(/\n/, $groups);
 
#output the username we're looking for ( to emulate groups better)
print ("$opt_u : ");
 
#where all the magic really happens
#split the array again, and output the first part of the split, as based
#on the strcuture of the /etc/groups file
foreach (@split_groups){
	my @temp_split= split(/:/, $_);
	print ("$temp_split[0] ");
}
 
#clean up 
print ("\n");
```

So after writing the code above originally, the interviewer looks things
over and asks me a couple of questions. I don't remember all of them,
the only one I can remember now ( almost two weeks later ) is below:

“Why are you using calling out instead of using a system call?”  

After looking around, PERL's systems calls abilities are fairly minimal.
I could open a file, and parse through it. But I figured why not save
myself some of the work and use the tools in the shell to ease my work.

Regardless, if you are in preparing for an interview maybe this might
give you a leg up. Or at least now other interviewers will have to start
using a different question.
