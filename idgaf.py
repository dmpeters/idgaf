from bottle import error, get, route, run, static_file, template, debug
from random import randrange, choice


# idgaf
@route('/')
@route('/<what>')
def idgaf(what='seriously'):
    # import pdb; pdb.set_trace()

    font_choices = ['Lato', 'Josefin Sans', 'Raleway']
    font = choice(font_choices)

    if what[0] == '-':
        copy = 'idgaf ' + what.strip('-') + '!'
    else:
        copy = what + ' idgaf!'
    copy = copy.upper()

    # Random color generator (http://pastebin.com/1XDgR45Q)
    bcolor = "#%s" % "".join([hex(randrange(0, 255))[2:] for i in range(3)])
    tcolor = "#%s" % "".join([hex(randrange(0, 128))[2:] for i in range(3)])

    return template('index.html.tpl', copy=copy, font=font,
                    tcolor=tcolor, bcolor=bcolor)

# static
@get('/<file:re:.*\.css>')
def css(file):
    return static_file(file, root='static')

# error
@error(404)
@error(500)
def error(code):
    # Random color generator (http://pastebin.com/1XDgR45Q)
    bcolor = "#%s" % "".join([hex(randrange(0, 255))[2:] for i in range(3)])
    tcolor = "#%s" % "".join([hex(randrange(0, 128))[2:] for i in range(3)])
    return template('index.html.tpl', copy='GFY!',
                    tcolor=tcolor, bcolor=bcolor)

# run
# debug(True)
run(reloader=True)