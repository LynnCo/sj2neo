# builtin
# external
import flask
import flask.ext.misaka as misaka
import flask.ext.scss as scss

app = flask.Flask(__name__)
misaka.Misaka(app)
scss.Scss(app, asset_dir='static')

@app.route('/')
def index (): return flask.render_template('paths/index.html')

@app.route('/static/<path:filename>')
def base_static(filename): return flask.send_from_directory(app.root_path + '/static/', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)