from bin.app import app, db
from flask import render_template, flash, redirect, url_for
from bin.app.forms import LoginForm, RegistrationForm
from bin.app.models import User
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/')
def home():
    return render_template("homepage.html")


@app.route('/index')
def index():
    user = {"username": "mapel"}
    posts = [{"author": {"username": "luson"}, "body": "save the child!"},
             {"author": {"username": "paidax"}, "body": "art is boom!"}]
    return render_template("index.html", user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("invalid username or password")
            return redirect(url_for("index"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("index"))
    return render_template("login.html", title="login", form=form)


@app.route('/loginout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='注册', form=form)


@app.route('/xiaoyaoyou')
def show_1():
    return app.send_static_file("xiaoyaoyou.txt")


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {"author": user, "body": "test1"},
        {"author": user, "body": "test2"}
    ]
    return render_template("user.html", user=user, posts=posts)


@app.route('/backend')
def administrators():
    return render_template("administrator.html")
