Title: Fedora, SELinux, Unbound, Oh My
Date: 2016-03-07
Author: Bryce
Tags: fedora,selinux,unbound
Slug: fedora-selinux-unbound

For a long time, I've wanted to upgrade my home network setup from using dnsmasq
resolving to Google's DNS, to an internally hosted dns service that can do
some extra things like DNSSEC. This past weekend I had a breif moment of free
time, so I decided to play with [Unbound](https://unbound.net/) on my spare Fedora 23 laptop.

I started with installing Unbound on the laptop, read up on Unbound from the
ArchLinux Wiki, a great resource for knowledge even if you're not running Arch,
and performing a basic internet search just to get exposed with how other
people setup Unbound. I found
[this blog post](https://calomel.org/unbound_dns.html)
that does a great job of walking someone through ....


To add for the forward section, I go into `/etc/unbound/conf.d/` and 
```
cp example-something.conf fowarder.conf
```

add the google DNS servers as recommended by the blog post, restart the service,
modify `/etc/resolv.conf`, and websites resolve without any issue. So far, so
good. Next up was adding DNS filtering, I followed the instruction from the
Arch Linux wiki, downloaded the file and copied it to
`/etc/unbound/local.d/adservers.conf`
tried restarting the service and got this error in the logs:
`STUB`

I go and review the permissions within the directory, they weren't correct,
after I fixed them I tried to restart the service again and I still see the
same error message.

![Photo]({attach}/images/jMN4ebSmbZdMA.gif)

After what felt like an hour and using every permissions trick I can think of,
I finally remembered that I was running with SELinux enabled. So I quickly try:

```
setenforce 0
```

restarted unbound, and BAM, Unbound is working again.

![Photo]({attach}/images/dpYkMt1b9BNmw.gif)

I now know that SELinux is causing the problem, now to figure out how to fix it.
I jump back to the command line and type a couple of commands:

```
cd /etc/unbound/conf.d
ls -liahZ
STUFF
cd ../local.d
ls-liahZ
MORE STUFF
```

because I downloaded the adservers.conf file from the
internet, instead of copying the example config and adding in the data
manually, I didn't get the correct SELinux label.
