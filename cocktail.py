from flask import Flask
from flask import render_template
from flask import request

from base64 import b64encode

# From https://stackoverflow.com/questions/9767585/insert-static-files-literally-into-jinja-templates-without-parsing-them
import jinja2

def include_file_data(name, **kwargs):
    return "data:;base64," + b64encode(render_template('custom/' + name, **kwargs).encode('utf-8')).decode('ascii')#.replace('\\', '\\\\').replace('\n', '\\n').replace('"', '\\"')

def include_file(name, **kwargs):
    return render_template('custom/' + name, **kwargs).replace('\\', '\\\\').replace('\n', '\\n').replace('"', '\\"')

app = Flask(__name__)

app.jinja_env.globals.update(include_file=include_file)
app.jinja_env.globals.update(include_file_data=include_file_data)

@app.route('/render/<name>', methods=['GET'])
def render(name=None):
    return render_template('custom/' + name, **request.args)

