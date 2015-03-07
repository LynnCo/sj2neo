# builtin
# external
import scss
import flask
import flask.ext.misaka as misaka

# basic flask app
app = flask.Flask(__name__)
# markdown
misaka.Misaka(app)
# scss
with open('sj2neo/static/scss/main.scss', 'r') as infile:
    scss_content = infile.read()
compiled_css = scss.Scss().compile(scss_content)
with open('sj2neo/static/css/main.css', 'w') as outfile:
    outfile.write(compiled_css)

@app.route('/')
def index (): return flask.render_template('paths/index.html')

@app.route('/static/<path:filename>')
def base_static(filename): return flask.send_from_directory(app.root_path + '/static/', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)