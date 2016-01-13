#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bryce'
SITENAME = u'scrollingtext.org'
SITEURL = 'http://%s' % SITENAME

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ATOM = 'feed/atom.xml'
FEED_RSS = 'feed/rss.xml'
TAG_FEED_ATOM = 'tag/%s/feed/atom.xml'
TAG_FEED_RSS = 'tag/%s/feed/rss.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/btv/'),
         ('Twitter', 'https://twitter.com/bryceverdier'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MD_EXTENSIONS = ['fenced_code',
                 'codehilite(css_class=highlight, linenums=True)',
                 'extra']
DEFAULT_CATEGORY = 'blog'
STATIC_PATHS = ['images']

