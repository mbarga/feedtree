# -*- coding: UTF-8 -*-

from flask import Flask
from flask import render_template
from authenticate.views import authentication
from visualization.views import visual


app = Flask(__name__)

app.register_blueprint(authentication)
app.register_blueprint(visual)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
