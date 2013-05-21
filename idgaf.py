from bottle import error, get, route, run, static_file, template, debug


# idgaf
@route('/')
@route('/<what>')
def idgaf(what='seriously'):
    import pdb; pdb.set_trace()

    if what[0] == '-':
        ughhh = 'idgaf ' + what.strip('-') + '!'
    else:
        ughhh = what + ' idgaf!'

    # fuuuu = template('index', ughhh=ughhh)
    # return fuuuu
    return ughhh


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