Title: Hiding Keyboard Input From the Screen
Date: 2010-03-02 07:21
Author: Bryce
Tags: PERL, Python, Terminal
Slug: hiding-keyboard-input-from-the-screen

For my current job I'm in charge of writing a script that requires a
person to input their password and me being the semi-security conscious
individual that I am knew that regular input for a script like this
would be bad, as that would allow for over the shoulder (literally) view
of someone's password. This is just unacceptable.

To solve this problem I hit the internets for a way to hide user input
in Perl script. And in my travels I came across this [old PERL FAQ
site](http://www.perl.com/doc/FAQs/FAQ/oldfaq-html/Q4.32.html). I
decided to try out the code and update it, throw it into a little dummy
script. This is what I got (minus the dummy script):

```perl
sub get_password
{
  print "enter your password: ";
  system("stty -echo");
  chop(my $password=<>);
  print "\n";
  system("stty echo");
 
  return $password;
}
```

Saved it, ran it, and Holy Missing Characters Batman, it worked. So just
as a mental exercise, I wanted to see if I could get it to emulate the
password request when you run sudo, and I wrote this up in Python
(because I need the practice):

```python
#!/usr/bin/python
 
import os
import getpass
 
def get_password():
    #print "Please enter your password:"
    os.system("stty -echo")
    password = raw_input( getpass.getuser() + "'s password")
    os.system("stty echo")
    print "\n"
 
    return password
 
def main():
    local_password = get_password()
    print local_password
 
main()
```

And again... it worked. Of course I finally realized that the reason why
it worked is because of the line "stty -echo". Taking that I typed it
into a standard terminal and after hitting enter the results were the
same. My terminal functioned normally, but without showing me the
characters I was typing. After returning my terminal back to normal I
decided to read a little more about stty. After digging through the man
page for a little while I came across this argument which is an alias
for echo:

```text
[-]crterase
echo erase characters as backspace-space-backspace
```

Thus the reason why I couldn't see anything change is because my
terminal is treating all characters I type on the screen as a three part
sequence of non alphanumeric characters. Although I find this a little
odd; I have to just go with the words of Bugs Bunny on this one, “I
don't ask questions. I just have fun.”
