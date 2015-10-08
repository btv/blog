Title: Windows 7 USB Boot Disk
Date: 2009-11-10 18:25
Author: Bryce
Tags: USB Bootdisk, Windows 7
Slug: windows-7-usb-boot-disk

So on your computer you have a shiny new copy of Windows 7 in ISO
format. Now the next question is how to get it unto your Asus EEE PC. A
USB Bootdisk of course (you could burn a dvdr, but why waste it). So
here is the procedure I had to follow to get mine to work.


Things you'll need:

USB drive \> 4GB

Windows 7 in iso format

UNetbootin [(link)](http://unetbootin.sourceforge.net/)

a running version of Vista

- 1) First step is to use UNetbootin to get the contents of the ISO onto
the usb drive.  

- 2) Wait while things are copied to the disk.  

- 3) Remove a couple of files from the USB disk after UNetbootin is done:

- 3.1) vesamenu.c32

- 3.2) syslinux.cfg

- 3.3) ubnfile.txt

- 3.4) ubnpath.txt

- 3.5) ldlinux.sys

- 3.6) bootmgr

- 4) Use whatever method your comfortable with to get the drive letter
for the device (In this we're going to say that my thumb drive is E:).

- 5) Now bring up your command line (usually Start Button -> Run & type
cmd then enter). And put the following instructions in it:

`bootsect /n60 e:`

- 6) Now close out the command window, safely disconnect the thumb drive,
and your ready to boot up windows 7 on that awesome EEE Pc of yours...
or someone else's.
