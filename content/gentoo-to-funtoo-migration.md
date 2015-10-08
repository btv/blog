Title: Gentoo to Funtoo Migration
Date: 2009-08-31 21:26
Author: Bryce
Tags: Funtoo, Gentoo, HowTo, Linux
Slug: gentoo-to-funtoo-migration

I have a little confession to make. I've been using Linux for a long
time now. Over ten years if you want to put a number to it. The last
seven of which I've been a devout
[Gentoo](http://en.wikipedia.org/wiki/Gentoo) user. And in being a fan
all those years and trolling on the forums like I usually do. I've seen
a lot of complaints over the slowness of portage (the package management
system for gentoo) and numerous requests for it to be rewritten to no
longer use rsync as its back end.

And while [Sabayon](http://en.wikipedia.org/wiki/Sabayon_Linux) has to
change this in their own distribution, which is based on gentoo and uses
subversion for the Sabayon packages above the regular gentoo packages.
There are also various layouts hosted by other gentoo users that
accomplish the same thing.Which is basically to use subversion above
portage. So even though this is a little different the actual portage
architecture hasn't really changed, its still done over rsync.

Recently it has come to my attention that the founder of Gentoo, [Daniel
Robbins](http://en.wikipedia.org/wiki/Daniel_Robbins), has started a new
distro based on his old creation. Its called
[Funtoo](http://www.funtoo.org). And one of the things about this that
caught my eye was that its using
[Git](http://en.wikipedia.org/wiki/Git_(software)) to do the package
updates. Well of course I had to try this out. So in a virtual machine I
got funtoo up and running. And I enjoyed the speed up of using git over
rsync. But of course the geek mind wanders, like it always does, and I
began to wonder if I could take a regular Gentoo install and move it to
Funtoo without having to reinstall everything. So out came the virtual
machine again, installed Gentoo on it. And this is my recipe for moving
a Gentoo box to a Funtoo box.

So, in order for someone to do this, they are going to need a couple of
things:

- 1) a working install of gentoo (DUH) as well as:  

- 1.1)have git emerged (installed)  

- 1.2)have the 2.2 version of portage installed  

- 2) a downloaded copy of the funtoo stage 3 build for your system

procedure:

(This part of the instructions where copied from the [Funtoo quick install](http://www.funtoo.org/en/articles/funtoo/quick-install-howto/))  

move /usr/portage to /usr/portage_old

download a copy of the [current funtoo's portage snapshot](http://dev.funtoo.org/linux/~funtoo/snapshots/portage-current.tar.bz2)
from the website and decompress the file in the /usr directory:

`cp portage*.tar.bz2 /usr`

`cd /usr`  

`tar zxjif portage-*.tar.bz2`

cd into the new portage directory and checkout the funtoo git repository:

`cd /usr/portage`  

`git checkout funtoo.org`

update portage data:

`emerge --sync`

After that I just did a simple system update (being this was a barebones
install of gentoo, system and world are the same. I can suspect that you
will have more to rebuild if this is not the case.) :  

`emerge -u system`

After this point, your going to be making the conversion from Gentoo to
Funtoo. So things are of course going to go as smooth as sandpaper.
Actually, it really wasn't that bad. There is just some loose ends
regarding networking that you need to tie up.

Go to where you have your funtoo tarball, and extract the net.lo file
like so:

`tar xvjif state3-arch-current.tar.bz2 ./etc/init.d/net.lo`

then copy it to your /etc like so:

`cp net.lo /etc/init.d/net.lo`

then delete net.eth0:  

`rm -f /etc/init.d/net.eth0`

and the last part is to make sure your using a version of dhcpcd >=
4.x. If your running 5.x, then all you have to do is:

`rc-update add dhcpcd default`

and your done.

If your not running dhcpcd 5x and portage only tells you the latest
version to install is in the 4x series, then you'll need to make a quick
modification to the package.keywords file:  

`echo "net-misc/dhcpcd ~x86" >> /etc/portage/package.keywords`

and then reemerge dhcpcd, afterwards you'll be able to do the rc-update
command above.

And if your using a static IP for your new Funtoo box, then you can
avoid all that hassle above and just follow the Funtoo Network guide
[here](http://funtoo.org/en/funtoo/networking/).

After this point your basically done. You might have to run a quick
etc-update. And maybe rebuild various packages. But all things said and
done, welcome to your new funtoo system. Now go enjoy those faster
sync's. ;)

Thanks for sticking around this long, and happy emerging.
