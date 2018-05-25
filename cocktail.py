from flask import Flask
from flask import render_template
from flask import request

# From https://stackoverflow.com/questions/9767585/insert-static-files-literally-into-jinja-templates-without-parsing-them
import jinja2

def include_file(name, **kwargs):
    return render_template('custom/' + name, **kwargs).replace('\\', '\\\\').replace('\n', '\\n').replace('"', '\\"')

app = Flask(__name__)

app.jinja_env.globals.update(include_file=include_file)

@app.route('/render/<name>', methods=['GET'])
def render(name=None):
    return render_template('custom/' + name, **request.args)

