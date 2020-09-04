from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# 实例化flask对象
app = Flask(__name__)
# 设置配置文件
app.config.from_object(Config)

# 绑定app和数据库
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "login"
from app import routes, models
