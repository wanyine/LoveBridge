from bottle import Bottle, view
app = Bottle()
# route, run, template, view, debug

@app.route('/hello/<name>')
@view('profile')
def index(name):
    return dict(name=name)
        #return template('<b>Hello {{name}}</b>!', name=name)
# run(host='localhost', port=8080)
