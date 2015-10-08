Title: Getting all installed software, and their versions, on Debian/Ubuntu
Date: 2010-04-21 15:57
Author: Bryce
Tags: Debian/Ubuntu, PERL
Slug: getting-all-installed-software-and-their-versions-on-debianubuntu

AAAHHH work! Everyone has those horror stories where your boss, or the
client, comes and asks for some horrible feature that will require an
entire rewrite of the program. Fortunately, that hasn't happened to me
(yet) and that is not what this blog entry is about. It's about the even
more (what I believe to be) unlikely scenario when someone wants a
feature that they think will be difficult to create and after some
research you implement that feature in a small amount of time. It's a
rare event and great confidence booster when it does happen though.

A co-worker wanted a feature added to a project. He thought that it
might take a while to complete so he talked to me first about it to
“plant the seed” and get my brain started on figuring out a solution,
not expecting a quick turnaround. Of course, as the title hints at, the
problem was to find out all the packages installed on our Debian boxes
as well as their version numbers. So after a little bit of googleing and
man page reading I had a basic algorithm to build on. Twenty minutes of
coding and testing later, I had this script:

```perl
#!/usr/bin/perl
#######################################################################
#	Created By: Bryce Verdier
#	on 4/14/10
# 
#	Function: grab all installed packages, find their exact
#           versions, and display them
#	NOTE: FOR USE ON DEBIAN BASED MACHINES
#######################################################################
 
my $temp_pack;
my $temp_ver;
my $returned_version;
my %pack_hash;
my @return = `dpkg --get-selections`;
 
foreach (@return)
{
  $_ =~ m/(\S*)[ \t].*/i;
 
  $temp_pack = $1;
 
  $returned_version = `dpkg -s $temp_pack`;
 
  $returned_version =~ m/Version: (.*)/i;
 
  $temp_ver = $1;
 
  $pack_hash{$temp_pack} = $temp_ver;
 
}
 
while((my $key, my $value) = each(%pack_hash))
{
  print "$key : $value\n";
}
```

I will admit that is a little slow (on my desktop it takes around two
and a half minutes to complete) and could probably benefit from some
parallelization. However, that might be over-engineering for such a
simple task. I'll code that feature up next, grab a stopwatch, and test
it just to find out. Anybody gonna place bets one way or another? In the
meantime, I'm proud of my use of regex's in this script, the "\\S"
removes the trailing whitespace from the package names, instead of just
using ".*", which should speed things up a bit because I don't have to
call chomp on each package name. Also using a hash for storage
simplifies the data management and should allow for an easier time
porting the code into a larger script later.
