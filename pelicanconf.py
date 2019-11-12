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
import render_html
JINJA_FILTERS = {
                    'sliders':my_filters.find_slider,
                    'striptags':my_filters.strip_tags,
                    'find':my_filters.findarticle,
                    'findbyslug': my_filters.findbyslug,
                    'see': my_filters.see,
                    # 'make_list': my_filters.make_list,

                    'main_menu': render_html.return_menu,
                    'getArticle': render_html.article_get,
                    # 'top_menu': render_html.top_menu,
                    # 'social_menu': render_html.social_menu,
                    # 'contact_menu': render_html.contact_menu,
}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
        },
        'markdown.extensions.extra': {},
        # optionally, more extensions,
        # e.g. markdown.extensions.meta
    },
    'output_format': 'html5',
}

THEME_OPTIONS = {
        'default': {
            'header': "dark"
        },
        'pages': {
            'header': "light"
        }
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# PATH = 'content'
# STATIC_PATHS = ['blog', 'downloads']
ARTICLE_SAVE_AS = 'blog/{slug}.html'
# ARTICLE_URL = '{date:%Y}/{slug}.html'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['make_list_of_articles']
PAGE_SAVE_AS = "pages/{slug}.html"
