Title: Getting the eeepc synaptic pad to work with Fedora 12
Date: 2010-02-17 07:08
Author: Bryce
Tags: Fedora 12, HowTo, Linux
Slug: getting-the-eeepc-synaptic-pad-to-work-with-fedora-12

![Photo]({attach}/images/Fedora_logo.svg)

Of all the how to's I've posted here over the last half year, this has
to be one of the easiest. But when I tried to figure this out on my own
it took a little bit of digging. So for the benefits of everyone else on
the interwebs here is a one stop shop for getting your synaptic pad to
work for your EEE-pc with Fedora 12.

Things you'll need:


I've found that xorg.conf for fedora 12 is not included with the default
install of fedora 12. Thus we need to get it; so while as root (or with
sudo) type:

`Xorg -configure :1`

After doing this you should now have an xorg.conf file in /etc/X11. The
second part is to now put a little extra configuration into the
xorg.conf file. Now using your favorite editor paste the following stuff
into the file. I have placed mine beneath the mouse section.

```text
Section "InputDevice"

Identifier "Synaptics"

Driver "synaptics"

Option "Device" "/dev/input/mice"

Option "Protocol" "auto-dev"

Option "Emulate3Buttons" "yes"

Option "SendCoreEvents" "true"

Option "TapButton1" "1"

Option "TapButton2" "2"

EndSection</code>
```

And for the last step, in the "ServerLayout" section we need to change
this line:

`InputDevice    "Mouse0" "CorePointer"`  

to this line:

`InputDevice    "Synaptics" "CorePointer"`

Save the changes, restart X (logging out and back in works well), and
now you can single and double finger taps working with ease.I
