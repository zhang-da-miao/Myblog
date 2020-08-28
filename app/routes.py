from app import app
from flask import render_template


@app.route('/hello/<name>/')
def hello(name):
    return 'Welecome %s' % name


@app.route('/')
@app.route('/index')
def index():
    user = {"username": "mapel"}
    posts = [{"author": {"username": "luson"}, "body": "save the child!"},
             {"author": {"username": "paidax"}, "body": "art is boom!"}]
    return render_template("index.html", title="Welecome", user=user, posts=posts)
