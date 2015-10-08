Title: 2600 article published
Date: 2009-11-04 02:41
Author: Bryce
Tags: 2600, NMAP
Slug: 2600-article-published

![Photo]({attach}/images/2600.gif)

So many moons ago, I wrote an article and submitted it to 2600. After a
two month wait they agreed to print it. At that point I was given the
idea and backing to start a blog. (So you primarily have 2600 to thank
for this blog. ;) ) I would have made that my first post, however the
agreement with 2600 is that if you get something accepted, you can't
republish the article somewhere else until after 2600 does. Finally,
almost eight months since when I first submitted the article, the
article is on the stands. Thus, here is the article:

How to ALMOST Hide Your Digital Identity While Port Scanning with Nmap
----------------------------------------------------------------------

For people in the know, port scanners are double edged swords. While it
gives System and Network administrators the ability to scan for unwanted
holes in their firewalls, servers, and computers, it also gives
malicious Internet users the ability to do the same thing. And is
usually the first step a would-be intruder takes to find a way into a
network. One of the most well known port scanner's is Nmap. Nmap is
known to run on Linux, FreeBSD, Mac OS X, Solaris, Windows, and more. So
chances are that no matter what OS you're running, you can run Nmap from
it.

DISCLAIMER: Just because you're about to learn a new tool today, does
not mean that you should go straight to work or school and just start
scanning every computer in sight. This is a real good way to make the
network administrators very angry. So be courteous; if you do not own
the computer you're about to scan, get permission. And this is for
educational purposes only, obviously.

I am quite sure that some of the people reading this article are more
adept with this tool than I am. (If your not, then I would recommend you
spend some time with it before continuing with this article... or not.)
For those who don't know Nmap has the ability to change its scanning IP,
and do the same trick with a group of IP's, or decoys as the manual
calls them. So for everyone who lives by their firewall logs, you might
want to start keeping a closer look at your logs concerning port scans,
because that IP that is scanning you is probably not the IP that you
think it is.

From the manual, there are two arguments that I will go into more depth:
-S and -D. -S has the explanation of, “-S <ip_address>: Spoof source
address”. And -D is described as, “-D <decoy1,decoy2[,me],...>: Cloak a
scan with decoys”(notice no space between the comma decoy1 and decoy2).
If you do use “ME” you will put in you're computer’s IP address as part
of the cycle of decoys. I do not know if you would want to do this, but
maybe you do. Anyway, let’s see some of these configurations in action:

```bash
sudo nmap -e eth0 -P0 -S 12.24.36.48 -A -T4 192.168.1.27
```

<code>
Starting Nmap 4.62 ( <http://nmap.org> ) at 2009-02-15 00:13 PST
Warning: OS detection for 192.168.1.27 will be MUCH less reliable
because we did not find at least 1 open and 1 closed TCP port
All 1697 scanned ports on mythbox (192.168.1.27) are filtered
MAC Address: 00:14:BF:5B:2D:5C (Cisco-Linksys)t
Too many fingerprints match this host to give specific OS details
Network Distance: 1 hop
Nmap finished: 1 IP address (1 host up) scanned in 36.634 seconds
</code>

This is just to show you what I typed at the command prompt, so you can
see how to use the -S argument and what to expect as possible results.
As I said above, -S is to spoof the IP address of the hosting machine,
which I have it set to spoof the IP address of 12.24.36.48. However, I
have a couple more arguments thrown in for good measure. First the “-e”
this is telling Nmap which network card to use. Generally, Nmap knows
which card to use however, I've decided to use it here to be explicit.
The next extra argument is “-P0”, this is to tell Nmap not to ping the
host as Nmap likes to ping before scanning to make sure the host is
online. Now that we've gone over the boring stuff, let's look at some
firewall logs.

<code>
Jun 13 20:37:01 mythbox IN=eth0 OUT=
MAC=00:14:bf:5b:2d:5c:00:13:d4:78:18:c6:08:00 SRC=12.24.36.48
DST=192.168.1.27 LEN=44 TOS=0x00 PREC=0x00 TTL=40 ID=63097 PROTO=TCP
SPT=43468 DPT=1383 WINDOW=1024 RES=0x00 SYN URGP=0

Jun 13 20:37:01 mythbox IN=eth0 OUT=
MAC=00:14:bf:5b:2d:5c:00:13:d4:78:18:c6:08:00 SRC=12.24.36.48
DST=192.168.1.27 LEN=44 TOS=0x00 PREC=0x00 TTL=47 ID=56142 PROTO=TCP
SPT=43469 DPT=722 WINDOW=4096 RES=0x00 SYN URGP=0
</code>

This output shows the results of using the command above has on my
iptables firewall log. If you look in the screen shot on each line
you'll see: "SRC=12.24.36.48". Which is the exact IP we set from the
command line. We know this works with a single IP address, but what
about multiple IP addresses?

```bash
sudo nmap -e eth0 -P0 -D 12.24.36.48,3.6.9.12,5.25.125.250 -A -T4
192.168.1.27
```

<code>
Starting Nmap 4.62 ( <http://nmap.org> ) at 2009-02-15 00:13 PST

Warning: OS detection for 192.168.1.27 will be MUCH less reliable
because we did not find at least 1 open and 1 closed TCP port

Interesting ports on mythbox (192.168.1.27):

Not shown: 1693 filtered ports

PORT STATE SERVICE VERSION

80/tcp open http lighttpd 1.4.15
631/tcp open ipp CUPS 1.2
6543/tcp open mythtv?
6544/tcp open mythtv?

MAC Address: 00:14:BF:5B:2D:5C (Cisco-Linksys)
Device type: general purpose
Running: Linux 2.6.X
OS details: Linux 2.6.9 - 2.6.12 (x86)

Uptime: 0.031 days (since Wed Jun 13 20:11:22 2007)

Network Distance: 1 hop

Nmap finished: 1 IP address (1 host up) scanned in 138.657 seconds
</code>

Just like the first command, we start Nmap telling it which network card
to use and instead of just specifying one IP address, we specify three
IP addresses, 12.24.36.48, 3.6.9.12, and 5.25.125.250. Now let’s take a
quick look at our iptables log and see what happens.

<code>
Jun 13 20:53:54 mythbox IN=eth0 OUT=
MAC=00:14:bf:5b:2d:5c:00:13:d4:78:18:c6:08:00 SRC=12.24.36.48
DST=192.168.1.27 LEN=44 TOS=0x00 PREC=0x00 TTL=43 ID=16809 PROTO=TCP
SPT=63815 DPT=234 WINDOW=4096 RES=0x00 SYN URGP=0

Jun 13 20:53:54 mythbox IN=eth0 OUT=
MAC=00:14:bf:5b:2d:5c:00:13:d4:78:18:c6:08:00 SRC=3.6.9.12
DST=192.168.1.27 LEN=44 TOS=0x00 PREC=0x00 TTL=42 ID=16809 PROTO=TCP
SPT=63815 DPT=234 WINDOW=3072 RES=0x00 SYN URGP=0

Jun 13 20:53:54 mythbox IN=eth0 OUT=
MAC=00:14:bf:5b:2d:5c:00:13:d4:78:18:c6:08:00 SRC=5.25.125.250
DST=192.168.1.27 LEN=44 TOS=0x00 PREC=0x00 TTL=42 ID=16809 PROTO=TCP
SPT=63815 DPT=234 WINDOW=3072 RES=0x00 SYN URGP=0
</code>

Well, well, well, just like the manual said, the firewall logs show that
access was attempted from our specified address above, in the exact
order that we inputted them. You can discover this for yourself by
looking at every other line from the screen shot, and noticing what SRC
equals on those lines.

So let's recap what we have (hopefully) learned today. We learned how to
change your IP address while scanning, as well as learned that you can
use an array of IP address to pretend to be other IP while scanning.

Additional Links:

- 1) Nmap website: <http://www.insecure.org/nmap/>

- 2) Performance: <http://www.insecure.org/nmap/man/man-performance.html>

- 3) Port Scanning Basics:
<http://www.insecure.org/nmap/man/man-port-scanning-basics.html>

- 4) Address Spoofing:
<http://www.insecure.org/nmap/man/man-bypass-firewalls-ids.html>
