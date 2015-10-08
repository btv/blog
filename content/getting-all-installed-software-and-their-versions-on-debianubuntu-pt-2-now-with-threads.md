Title: Getting all installed software, and their versions, on Debian/Ubuntu pt 2: Now with Threads!
Date: 2010-05-07 01:38
Author: Bryce
Tags: Debian/Ubuntu, Mutlti-Threading, PERL
Slug: getting-all-installed-software-and-their-versions-on-debianubuntu-pt-2-now-with-threads

Even though Poisonbit's solution to the original problem is the fastest
(Thanks again PoisenBit!) I decided to use the original code as an
excuse to learn multi-threading programming in PERL and see if it might
improve the performance of the original code. One of those "for shits
and giggles" moments.

First off, here is the new and improved code:

```perl
#!/usr/bin/perl
#######################################################################
#	Created By: Bryce Verdier
#	on 4/14/10
# 
#	Function: grab all installed packages, using threads
#           find their exact versions, and display them
#	NOTE: FOR USE ON DEBIAN BASED MACHINES
#######################################################################
 
use threads;
 
my $temp_pack;
my $temp_ver;
my $returned_version;
my %pack_hash :shared;
my $thread_count = 0;
my $pack_count;
my @return = `dpkg --get-selections`;
 
sub get_package_ver
{
  my %args = @_;
  my $temp_ver;
  my $returned_ver = `dpkg -s $args{package}`;
 
  $returned_ver =~ m/^Version: (.+)$/m;
 
  $temp_ver = $1;
 
  lock($args{hash});
  $args{hash}{$args{package}} = $temp_ver;
}
 
foreach (@return)
{
  $_ =~ m/^(\S+)[ \t].*/;
 
  $_ = $1;
}
 
 
$pack_count = @return;
while ( $pack_count - $thread_count >= 1)
{
    my $th1 = threads->create(\&get_package_ver, hash => \%pack_hash, 
                              package => $return[$thread_count]);
    my $th2 = threads->create(\&get_package_ver, hash => \%pack_hash, 
                              package => $return[$thread_count+1]);
 
    $th1->join();
    $th2->join();
 
    $thread_count = $thread_count + 2;
}
 
# Get the odd package, if there is one
if ($pack_count - $thread_count == 1)
{
    my $th1 = threads->create(\&get_package_ver, hash => \%pack_hash, 
                              package => $return[$thread_count]);
 
    $th1->join();
 
    $thread_count++;
}
 
while((my $key, my $value) = each(%pack_hash))
{
  print "$key : $value\n";
}
```

For all the number crunchers out there, putting things into two threads
reduced the program execution time by more than 1 minute. For a program
that took two and a half seconds to complete, a reduction to one and a
half seconds is pretty significant.Well, in my book anyway.

After first following the suggestions of Sam for the regexes, (Thanks
again Sam!) I pulled out the version checking code into its own function
so that each thread would have a very specific thing to do. After that I
realized I needed to clean up the package names that were being sent to
the threads, creating the foreach loop on line 35. Within the foreach
loop I tried something that I didn't expect to work - the line:

```perl
$_ = $1;
```

There isn't a reason for the line above to not work, but in the PERL
code I've seen "\$\_" is not being used as a pointer to write data to,
only to retrieve data from. And I guess that is why I did not expect it
to work. But then, that's why I'm doing this - to learn things. :-D

After these changes and adding the threads code, I was almost done. For
some reason the data from each thread wasn't getting stored into the
hash. It wasn't until I looked a little deeper at the examples on
perldoc that I saw what I needed to do. In the section "Shared And
Unshared Data" I noticed I needed to mark %pack\_hash as shared, so all
the threads could access it. Which I did like so:

```perl
my %pack_hash :shared;
```

All in all, my first multi-threading coding expirence in perl wasn't
bad. Granted the program isn't complicated, but this was truely new
territory for me. I haven't tried doing any kind of
multi-process/multi-threading programming since my operating systems
class almost 3 years ago, so there were some battles to fight in my head
on how to modify things to work with multiple threads. But again, it was
a good experience. And I'm going to reiterate this so everyone
remembers: don't use this code in production. Poisonbit's solution is
MUCH faster than mine. Like me, use this code for learning.
