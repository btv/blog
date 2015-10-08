Title: Prime Number Generator Project Pt. 1
Date: 2009-08-14 21:47
Author: Bryce
Tags: C code, Programming Projects
Slug: prime-number-generator-project-pt-1

*NOTE: Sorry for the delay in posting. School is hitting me rather hard
as of late, and will continue too until the end of the month. Thus until
September posts are going to be a little sporadic... unfortunately. :(*

</p>

I'm fascinated with the idea of doing real world calculations on the
GPU. The idea just seems to make sense to me. You have this piece of
hardware in almost all machines today that is around to do one thing
really quickly, and that thing is to crunch numbers so video games can
look good. And unless your playing video games that card is mostly
sitting in the background just sucking up energy and maybe helping to
provide some[nice eye candy for you
desktop](http://www.youtube.com/watch?v=Y4wB3GUemVw&feature=related).

</p>

But within the last couple of years this idea has been changing. People
are figuring out ways to make this super calculator to do more general
purpose math manipulations. And now you have the idea of
[GPGPU](http://gpgpu.org/<br%20/></p><p>), which means General Purpose
computation on Graphics Processing Units. And of course like a good
geek, I want to play with this.

</p>

Of course, before I start to play
with[CUDA](http://en.wikipedia.org/wiki/CUDA<br%20/></p><p>), I needed
to come up with a baseline. Which leads me to ask myself, “What am I
going to program?” After some time, I decided I would program a prime
number generator. My next step was to code up a basic prime number
generator, using just a simple algorithm.

</p>
<p>
<script src="http://bitbucket.org/btv/square_root/src/c148c89faa79/normal/normal.c?embed=t"></script>

Again, nothing very special going on here. Taking some basic liberties
with calculations, like just giving the value of 2 & 3 as prime, and
starting to run calculations after 3. Also avoiding all calculations of
even numbers. Pretty simple stuff. And I'm positive that if I wanted to
I could tweak the current algorithm some more to squeeze an extra drop
or two of performance out of it. But that wasn't the point of this. This
program above is to just give me a baseline of performance . So as I now
start to play with CUDA and GPGPU I can get an idea on how much
performance might be gained.

</p>

And of course, what would be the point of creating a baseline if I din't
include the numbers of running this program.

</p>

<table>
</p>
<p>
<tr>
</p>
<p>
<td>
Iterations

</td>
</p>
<p>
<td>
Times (in seconds)

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td>
10

</td>
</p>
<p>
<td>
.001

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td>
100

</td>
</p>
<p>
<td>
.001

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td>
1000

</td>
</p>
<p>
<td>
.002

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td>
10000

</td>
</p>
<p>
<td>
.018

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td>
50000

</td>
</p>
<p>
<td>
.343

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td>
1000000

</td>
</p>
<p>
<td>
1.570

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td>
5000000

</td>
</p>
<p>
<td>
30.760

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td>
750000

</td>
</p>
<p>
<td>
64.410

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td>
1000000

</td>
</p>
<p>
<td>
109.660

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td>
5000000

</td>
</p>
<p>
<td>
2301.504

</td>
</p>
<p>
</tr>
</p>
<p>
<tr>
</p>
<p>
<td>
10000000

</td>
</p>
<p>
<td>
8713.000

</td>
</p>
<p>
</tr>
</p>
<p>
</table>
</p>

And as the table shows, not only is the code simple... its get to be
really slow with a really large number.

</p>

Next stop; somehow putting this code into CUDA and seeing what kind of
performance improvement can be derived.

</p>

