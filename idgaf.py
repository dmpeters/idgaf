#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import error, get, route, run, static_file, template, debug
from random import randrange, choice
from string import ascii_letters, digits
import redis

# redis
rdb = redis.StrictRedis(host='localhost', port=6379, db=0)

# idgaf
@route('/')
@route('/<what>')
def idgaf(what='seriously'):
    if what[0] == '!':
        copy = rdb.get(what)
        surl = what
    else:
        if what[0] == '-':
            copy = 'idgaf ' + what.strip('-') + '!'
        else:
            copy = what + ' idgaf!'

        # save to redis
        surl = '!' + _short()
        rdb.set(surl, copy)
        rdb.expire(surl, 2600000)

    return template('index.html.tpl',
                    copy=copy.upper(),
                    font=_choose_font(),
                    tcolor=_generate_colors('tcolor'),
                    bcolor=_generate_colors('bcolor'),
                    surl=surl)

# static
@get('/<file:re:.*\.css>')
def css(file):
    return static_file(file, root='static')

# error
@error(404)
@error(500)
def error(code):
    return template('index.html.tpl',
                    copy='SERIOUSLY GFY!',
                    font=_choose_font(),
                    tcolor=_generate_colors('tcolor'),
                    bcolor=_generate_colors('bcolor'))

# private (helper) methods
def _generate_colors(type):
    if type=='bcolor':
        return "#%s" % "".join([hex(randrange(0, 255))[2:] for i in range(3)])
    if type=='tcolor':
        return "#%s" % "".join([hex(randrange(0, 128))[2:] for i in range(3)])
    colors = ['#FFFFFF', '#000000', '#FF0000', '0000FF', '#C0C0C0']
    return choice(colors)

def _choose_font():
    font_choices = ['Lato', 'Josefin Sans', 'Raleway']
    return choice(font_choices)

def _short():
    return ''.join(choice(ascii_letters + digits) for x in range(6))

# run
# debug(True)
run(reloader=True)
