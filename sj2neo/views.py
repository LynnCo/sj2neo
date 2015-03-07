# builtin
# external
import flask
import flask.ext.misaka as misaka
import flask.ext.scss as scss

app = flask.Flask(__name__, static_folder='static', static_url_path='')
misaka.Misaka(app)

@app.route('/')
def index ():
    return flask.render_template('paths/index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)