import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = "mapel10086"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mapel10086@localhost:3306/flaskblog?charset=utf8'

    SQLALCHEMY_TRACK_MODIFICATIONS = False