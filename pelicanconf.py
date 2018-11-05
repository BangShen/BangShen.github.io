#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Shen Bang'
SITENAME = "Shen Bang"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Linkedin', 'https://www.linkedin.com/in/bang-shen/'),
          ('Github', 'https://github.com/BangShen'),
          ('Zhihu','https://www.zhihu.com/people/chen-bang-61-78/activities'),)
DEFAULT_DATE_FORMAT = ('%a %d %B %Y')

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
THEME = 'foundation-default-colours'
DIRECT_TEMPLATES = (('index', 'archives'))