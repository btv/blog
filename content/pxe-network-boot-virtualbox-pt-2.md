Title: PXE Network Boot VirtualBox, PT 2
Date: 2010-03-26 08:40
Author: Bryce
Tags: PXE, VirtualBox
Slug: pxe-network-boot-virtualbox-pt-2

I have a project for work that involves setting up Debian's Fully
Automated Install (FAI) for a new server type that the company plans to
roll out. The server is a 4U chassis, which holds 36 hard drives in it.
And I am in charge of seeing if we can use a small 8 GB SSD for  the
root partition. I've been figuring out FAI for the past couple of
nights, but today my hardware disappeared. So until it returns - its off
on a quest at the moment -  I figured I would try and to use VirtualBox
to continue testing.

I started by creating a new machine in VirtualBox, 8GB drive, 1024 MB of
RAM, and that is when I realized I didn't have the foggiest idea how to
get VirtualBox to PXE boot. So off to the interwebs I went, searching
for an answer. And in my travels I came across a [great blog post that
had my
answer](http://www.bgevolution.com/blog/pxe-network-boot-virtualbox/).I
followed the instructions and started the machine. PXE booted up no
problem, but DHCP timed out. I was a little bummed by the immediate
failure, but like a good geek I persisted to find a solution, which I am
sharing below:

What you need:

A virtual machine created [(A new one will probably work
better)](<http://lifehacker.com/5204434/the-beginners-guide-to-creating-virtual-machines-with-virtualbox)

Click on the setting for your virtual machine you wish to PXE boot
with.

Select the “Network” tab. It give you a picture like this:

![Photo]({attach}/images/virtual-box-network-1.png)

Now click on the “Attachted To:” button and move it down to “Bridged
Adapter”. Like so:

![Photo]({attach}/images/virtual-box-network-2.png)

And finally,  (if it isn't already set up correctly for you), select
“Name” to be your working network card.

Again, credit for the initial write up go to Noah Seidman whose initial
blog post got me going. You write a lot of good technical articles Noah,
keep up the good work! I just wanted to explicitly state how to get this
last part of your tutorial working in case someone did not know how to
do it themselves.
