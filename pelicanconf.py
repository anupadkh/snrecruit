#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
cwd = os.getcwd()

AUTHOR = u'anupadkh'
SITENAME = u'SNRecruit'
SITEURL = ''
THEME = os.path.join(cwd,'templates','canvas')
PATH = 'content'
ARTICLE_PATHS = ['home', 'partners']
STATIC_PATHS = ['downloads','images']

TIMEZONE = 'Asia/Kathmandu'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
import sys
sys.path.append('.')

import my_filters
JINJA_FILTERS = {
                    'sliders':my_filters.find_slider,
                    'striptags':my_filters.strip_tags,
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# PATH = 'content'
# STATIC_PATHS = ['blog', 'downloads']
# ARTICLE_PATHS = ['blog']
# ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
# ARTICLE_URL = '{date:%Y}/{slug}.html'
