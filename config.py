"""
配置文件，默认
{
    'DEBUG':                                get_debug_flag(default=False),  是否开启Debug模式
    'TESTING':                              False,                          是否开启测试模式
    'PROPAGATE_EXCEPTIONS':                 None,
    'PRESERVE_CONTEXT_ON_EXCEPTION':        None,
    'SECRET_KEY':                           None,
    'PERMANENT_SESSION_LIFETIME':           timedelta(days=31),
    'USE_X_SENDFILE':                       False,
    'LOGGER_NAME':                          None,
    'LOGGER_HANDLER_POLICY':               'always',
    'SERVER_NAME':                          None,
    'APPLICATION_ROOT':                     None,
    'SESSION_COOKIE_NAME':                  'session',
    'SESSION_COOKIE_DOMAIN':                None,
    'SESSION_COOKIE_PATH':                  None,
    'SESSION_COOKIE_HTTPONLY':              True,
    'SESSION_COOKIE_SECURE':                False,
    'SESSION_REFRESH_EACH_REQUEST':         True,
    'MAX_CONTENT_LENGTH':                   None,
    'SEND_FILE_MAX_AGE_DEFAULT':            timedelta(hours=12),
    'TRAP_BAD_REQUEST_ERRORS':              False,
    'TRAP_HTTP_EXCEPTIONS':                 False,
    'EXPLAIN_TEMPLATE_LOADING':             False,
    'PREFERRED_URL_SCHEME':                 'http',
    'JSON_AS_ASCII':                        True,
    'JSON_SORT_KEYS':                       True,
    'JSONIFY_PRETTYPRINT_REGULAR':          True,
    'JSONIFY_MIMETYPE':                     'application/json',
    'TEMPLATES_AUTO_RELOAD':                None,
}
"""
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # 密钥
    SECRET_KEY = "never-guess"
    # mysql+pymysql://数据库用户名：密码2数据库地址：端口号/数据库名称？数据库格式
    # 其中数据库需要提前创建好
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mapel10086@localhost:3306/myblog?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
