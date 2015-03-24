#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from jinja2 import Environment, Template, contextfilter, evalcontextfilter

AUTHOR = 'Tristian Azuara'
SITENAME = 'tristianazuara'
SITEURL = 'triztian.github.io'

TIMEZONE = 'America/Phoenix'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Brennan Dunn', 'http://brennandunn.com/'),
          ('Kalzumeus', 'http://www.kalzumeus.com/blog/'),
          ('Nathan Barry', 'http://nathanbarry.com/'),
          ('IWTR', 'http://www.iwillteachyoutoberich.com/'),
          ('Copyhackers', 'http://copyhackers.com/'),
          ('Matt Might', 'http://matt.might.net/articles/'),
          ('ConsultingSuccess', 'http://www.consultingsuccess.com/'))

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/aztristian'),
          ('Github', 'https://github.com/Triztian?tab=repositories'),
          ('Stack Exchange', 'http://careers.stackoverflow.com/tristian'))
          

TAGS = {
    'Javascript': 'https://en.wikipedia.org/wiki/JavaScript',
    'Python': 'https://www.python.org/',
    'HTML': 'http://www.html5rocks.com/en/',
    'TrytonERP': 'http://www.tryton.org/',
    'Java': 'https://www.java.com/en/download/whatis_java.jsp',
    'PHP': 'http://php.net/',
    'Wordpress': 'https://wordpress.org/',
    'RequireJS': 'http://requirejs.org/',
    'Backbone.js': 'http://backbonejs.org/',
    'Bootstrap3': 'http://getbootstrap.com/',
    'matplotlib': 'http://matplotlib.org/',
    'chart.js': 'http://www.chartjs.org/',
    'Tomcat': 'https://tomcat.apache.org/',
    'Jersey': 'https://jersey.java.net/',
    'MySQL': 'https://www.mysql.com/',
    'Grunt.js': 'http://gruntjs.com/',
    'handlebars.js': 'http://handlebarsjs.com/', 
    'Zurb-foundation': 'http://foundation.zurb.com/'
}

THEME = "/Users/Tristian/Projects/triztian.github.io/theme"

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


@contextfilter
def jinja_eval(context, template):
    return Template(template).render(context)

JINJA_FILTERS = {
    'jinjaeval': jinja_eval 
}
