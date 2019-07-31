# EXERCISE: Implement View to display index.html with localhost:5000/hello ================

from flask import render_template
from flask_bootstrap import Bootstrap
from application import app

bootstrap = Bootstrap(app)


@app.route('/hello')
def hello():
    return render_template('index.html')
# ========================================================================
