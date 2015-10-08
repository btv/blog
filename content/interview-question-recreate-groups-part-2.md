Title: Interview question: Recreate groups PART 2
Date: 2010-03-13 05:32
Author: Bryce
Tags: PERL
Slug: interview-question-recreate-groups-part-2

In a previous post you might have noticed that I wrote some code that
was incomplete. (Thanks Dave for pointing that out! Greatly
Appreciated!) And now that some time has passed, and my life has calmed
down enough to give this another shot, here is my new version of the
code.

You might notice that a lot has changed since the last version. Most
importantly, I got rid of going the a shell out, as it has been taught
to me that there are security concerns with doing so. You should also
notice that I'm using regex's to do the filtering, I'm sure these could
be tightened down a little bit. But I won't get better with them unless
I at least start using them. I'm also getting the default group id of
the user, and returning that first in the output. And finally, I am
doing some error checking to make sure that the account is actually in
the system; something my previous script did not check for.

All in all, I'm happier with this script than the first version. And of
course, I'm interested in seeing if anyone can find out other bugs that
exist inside the code.

```perl
#!/usr/bin/perl
#######################################################################
#	Created By: Bryce Verdier
#	on 1/19/10
#       modified to fix errors 3/12/2010
#	Function: rework the output of the unix groups command
#	NOTE: FOR USE ON UNIX MACHINES!
#######################################################################
 
use warnings;
use strict;
use Getopt::Std;
 
sub get_gid
{
  my ($name) = @_;
 
  return getgrnam($name);
}
 
sub open_and_parse
{
  my ($in_user, $in_gid) = @_;
  my $guid_name;
  my @split;
  my @parse_groups;
  my @end_array;
 
 
  open(PASSWD, "/etc/group");
  while(<PASSWD>){
 
    # This line is to grab the default in_gid name
    if ( $_ =~ m/^.*\:$in_gid\:\:*/ ){
      @split = split(':', $_);
      $guid_name = $split[0];
    }
 
    # This line is to grab any line which has the in_user in it
    # while also rejecting the line with the in_gid number in it 
    elsif ( $_ =~ m/^.*$in_user.*/ ){
      @split = split(':', $_);
      next if ( $split[2] == $in_gid );
      push (@parse_groups, $split[0]);
    }
 
    # we don't care about anything else so skip it
    else{
      next;
    }
  }
 
  push ( @end_array, $guid_name);
  push ( @end_array, @parse_groups);
 
  return @end_array;
}
 
 
## Main script starts here
our($opt_u);
getopts('u:');
 
my $gid = get_gid($opt_u);
 
if ( defined($gid) ) {
  my @groups = open_and_parse($opt_u, $gid);
  print "$opt_u : @groups\n";
}else{
  print "$0: $opt_u: No such user\n";
}
 
exit 0;
```
