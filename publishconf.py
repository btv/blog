#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITENAME = u'pelican.scrollingtext.org'
SITEURL = 'http://%s' % SITENAME
RELATIVE_URLS = False

#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'


DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "scrollingtext"
#GOOGLE_ANALYTICS = ""
PIWIK_URL = "analytics.scrollingtext.org"
PIWIK_SITE_ID = '2'
