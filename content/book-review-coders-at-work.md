Title: Book Review - Coders At Work
Date: 2012-08-28 17:01
Author: Bryce
Tags: Book Reviews
Slug: book-review-coders-at-work

![Photo]({attach}/images/cow.png)

I just finished reading the book [*Coders at
Work*](https://en.wikipedia.org/wiki/Coders_at_work) by [Peter
Seibel](https://twitter.com/#!/peterseibel). This wonderful book is
filled with interviews with prominent programmers: Joe Armstrong, Simon
Peyton Jones, Donald Knuth, among others. My review isn't going to be
the standard book review. Instead I'm going to talk about some of the
specific ideas I picked up while reading the book and discuss those
ideas, rather than the book itself. For those of you who are looking for
more of a standard review, all I can really say is that Coders at Work
is well worth the time for a programmer or a computer
historian/hobbyist. Unfortunately for the casual non-computer-field
reader, the interview topics (and the interviewees) assume a certain
level of prior knowledge. What makes this book so good is that different
people will be able to walk away from it with different ideas, depending
on their areas of expertise and interest. As the industry grows and
changes, we definitely do things based on what the people before us have
already discovered - Seibel’s interview subjects are the fascinating
programmers whose ideas and hard work make possible all the cool things
we get to play with today.

Code Readings:

In the interview with [Douglas
Crockford](http://en.wikipedia.org/wiki/Douglas_Crockford) there was a
lot of talk about code readings. If you’re not sure what those are (I
wasn’t), from the way Douglas describes it they are regular meetings
where programmers read the code base together. In my mind it sounds like
someone is giving a presentation but instead of it being PowerPoint
slides, it’s code. I picture the presenter going line by line and
describing what is going on and why he or she decided to do things a
particular way. These sound like an excellent idea to me. In my
experience so far, the code review process seems to have been relegated
to using [Reviewboard](http://www.reviewboard.org/) or other similar
website-based tools. I'm not trying to insult these tools, but they
remove the human factor of the code review and hinder the discussion
that can happen over a particular piece of code. I understand that
programmer time is expensive and managers should be careful how much of
that time is spent in meetings. But I think these meetings could benefit
everyone and will have a return on investment (that is the time spent)
in ways that cannot be quickly seen. One benefit is that everyone who
attends will come out with a basic idea of what the code looks like
within a given project, even if they’re not working on that project
directly. So if things shift around (as they inevitably do) and a new
person is moved into that project, he or she won’t be starting from
scratch. Even just a little bit of knowledge might help a programmer get
over the initial shock of having to dive into a new project.

Programmers need Empathy:

In the interview with [Joshua
Bloch](http://en.wikipedia.org/wiki/Joshua_Bloch) there was a quick chat
about programmer personalities. There were a couple of choice quotes
regarding programmer empathy for the users, like, “...intelligence is
not a scalar quantity; it’s a vector quantity. And if you lack empathy
or emotional intelligence, then you shouldn’t be designing APIs or GUIs
or languages.” and “What we’re doing is an aesthetic pursuit. It
involves craftsmanship as well as mathematics and it involves people
skills and prose skills—all of these things that we don’t necessarily
think of as engineering but without which I don’t think you’ll ever be a
really good engineer.”

I bring these quotes up because I agree with them, and because they
speak of issues that are largely ignored in the engineering community
(again, in my experience). I've sure we’ve all run into programmers that
only care about the technical aspects of the project or the correctness
of their code and do not concern themselves for how the user might
interact with the system. For example, the company I work for designed a
web-app that included separate “Kill” and “Terminate” buttons. This was
a complete UI fail that could have been avoided, had the programmer
(we’ll call him/her “Terry”) had empathy for the user. As a programmer,
I understand the difference between
[SIGKILL](https://en.wikipedia.org/wiki/SIGKILL) and
[SIGTERM](https://en.wikipedia.org/wiki/SIGTERM), but those buttons
would be confusing to even the more-advanced-than-average user (and go
far beyond failing [the grandmother
test](http://www.urbandictionary.com/define.php?term=Grandma+Test)).
When this was brought up as a ticket for “Terry” to fix, “Terry” argued
that there was nothing technically incorrect about the problem and
closed the ticket “Won't Fix.”

Hiring:

One thing I noticed in a lot of the interviews was that Peter asked the
interviewee what he or she looked for in a potential new hire. What I
found fascinating is that none of them said, “I like to ask really hard
questions.” or “I ask really obscure questions about the programming
language they use to see how well they know it.” They mostly talked
about looking for someone who had passion for the craft.

As someone who is frequently on both sides of the hiring table, I know
that the current hiring process in Silicon Valley doesn't normally ask
questions about WHO is being hired. Questions about hobbies or interests
are rare. It's mostly just technical questions, as if the person who is
applying for the job is another computer whose sole purpose is to solve
a company's problems. All the emphasis seems to be focused on the
technical skills of the interviewee. While it's important to know if
someone can “do the job,” tech skills alone do not make a person a great
programmer - a good one, yes, but I don’t get the impression that
companies are settling for “good” anymore. Passion is what gives someone
the tenacity to work through the obstacles and become a great
programmer, and if we as interviewers insist on focusing only on hard
skills, we risk cheating ourselves out of the truly great engineers.

Donald Knuth:

Peter also asked every single interviewee about Donald Knuth's books and
his “literate programming” style of writing code. I will admit that I have
not read his books, but I want to. I'm not sure what this literate Programming
style is, but I'm curious enough about it to learn, and see if there are some
aspects of it I can incorporate into my own coding and documentation style. Next
step, pick up an electronic version of the book, [“Literate
Programming”](https://en.wikipedia.org/wiki/Literate_programming) and
give it a good read.

I fully enjoyed Coders at Work. I took away much more from the
interviews than I talked about here, and I’m sure there’s even more to
learn. I'm planning on rereading it again in a couple of years; as I
grow as a programmer I will have a different perspective on the craft,
and might find a whole new or different set of lessons from what I got
this time. If not, at the very least I’ll have the pleasure of reading
it again.
