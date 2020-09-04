from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from hashlib import md5


class User(UserMixin, db.Model):
    """定义模型，建立对应关系"""
    # 定义表名
    __tablename__ = "user"
    # 定义对象
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True, unique=True)
    email = db.Column(db.String(30), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(150))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    # 显示一个可读字符串，非必要
    def __repr__(self):
        return '<username:{}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True, unique=True)
    author = db.Column(db.String(20), index=True, unique=True)
    article_title = db.Column(db.String(20), index=True, unique=True)
    # 长文本
    article_body = db.Column(db.Text, index=False, unique=False)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
