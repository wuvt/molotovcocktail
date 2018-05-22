from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/render/<name>', methods=['GET'])
def render(name=None):
    return render_template('custom/' + name, **request.args)

