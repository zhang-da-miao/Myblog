from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm, EditProfileForm, ArticleForm
from app.models import User, Article
from flask_login import current_user, login_user, logout_user, login_required
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", user=user)


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
    print(form.result.data)
    print(type(form.result.data))
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("注册成功")
        return redirect(url_for('login'))
    return render_template('register.html', title='注册', form=form)


@app.route('/xiaoyaoyou')
def show_1():
    """静态文件展示"""
    return app.send_static_file("xiaoyaoyou.txt")


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    article = Article.query.filter_by(username=username).first_or_404()
    return render_template("user.html", user=user, article=article)


@app.route('/backend')
def administrators():
    """后台管理界面"""
    return render_template("administrator.html")


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('已修改')
        return redirect(url_for("edit_profile"))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='个人编辑资料', form=form)


@app.route('/article', methods=['GET', 'POST'])
@login_required
def article():
    form = ArticleForm()
    if form.validate_on_submit():
        article = Article(username=current_user.username, author=form.author.data, article_title=form.title.data,
                          article_body=form.article.data)
        db.session.add(article)
        db.session.commit()
        flash('已发布')
        return redirect(url_for("index"))
    return render_template('article.html', title='新建文章', form=form)


@app.route('/article/<article_title>')
@login_required
def show(article_title):
    article = Article.query.filter_by(article_title=article_title).first_or_404()
    return render_template('show.html', title=article.article_title, body=article.article_body, author=article.author)


@app.route('/revise/<article_title>', methods=['GET', 'POST'])
@login_required
def revise(article_title):
    form = ArticleForm()
    article = Article.query.filter_by(article_title=article_title).first_or_404()
    if form.validate_on_submit():
        article.author = form.author.data
        article.article_title = form.title.data
        article.article_body = form.article.data
        db.session.commit()
        flash('已修改')
        return redirect(url_for("index"))
    elif request.method == 'GET':
        form.author.data = article.author
        form.title.data = article.article_title
        form.article.data = article.article_body
    return render_template('article.html', title='修改文章', form=form)
