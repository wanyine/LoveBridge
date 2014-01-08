import random
from bottle import Bottle, view
app = Bottle()
# route, run, template, view, debug

@app.route('/')
@view('profile')
def index():
    name = ''.join(random.sample('abcdefgh', 3))
    return dict(name=name)
        #return template('<b>Hello {{name}}</b>!', name=name)
# run(host='localhost', port=8080)
