from bottle import error, get, route, run, static_file, template, debug
from random import randrange

# idgaf
@route('/')
@route('/<what>')
def idgaf(what='seriously'):
    # import pdb; pdb.set_trace()
    o = {}

    if what[0] == '-':
        copy = 'idgaf ' + what.strip('-') + '!'
    else:
        copy = what + ' idgaf!'

    o['copy'] = copy.upper()
    o['text_color'] = '#ffffff'
    o['body_color'] = "%s" % "".join([hex(randrange(0, 255))[2:] for i in range(3)])

    return template('index.html.tpl', o=o)


# static
@get('/<file:re:.*\.css>')
def css(file):
    return static_file(file, root='static')


# error
@error(404)
@error(500)
def error(code):
    return 'GFY!'


# run
# debug(True)
run(reloader=True)