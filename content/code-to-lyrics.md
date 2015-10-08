Title: Code to lyrics
Date: 2010-10-22 22:09
Author: Bryce
Tags: Humor, Personal, Python
Slug: code-to-lyrics

It's not everyday that one can turn song lyrics into code. I've been a
big fan of the group One Minute Silence for a pretty long time (1998 if
memory serves me correctly), but it wasn't until recently that I was
listening to the song “I Can Change” that I noticed that the spoken word
part that happens at both the beginning and the end of the song followed
a pattern. Noticing this pattern I realized I could reproduce the lyrics
in code:

```python3
#!/usr/bin/python3
 
def print_lyrics(words):
    if "I" in words:
        print("If I can change " + words[0] + ", " + words[1] + " can change.")
    else:
        print("If I can change " + words[0] + ", I can change " + words[1] + ",")
 
if __name__ == "__main__":
    number = [ str(2 ** x) for x in range(0,4)]
    number2 = number[1:]
    number2.append('I')
    for x in zip(number, number2):
        print_lyrics(x)
```

As a side note, I'm not sure if Yap intended to follow the powers of
two, but it worked out really well when trying to generate the numerical
output. And if you think your the kind of person that enjoys that
hip-hop metal with anti-capitalist message, then you might want to give
the song a try, and maybe the rest of their material if you like it.

Oh yeah, before I forget, Happy Friday everyone.
