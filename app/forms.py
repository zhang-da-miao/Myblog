from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length, NumberRange
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(message='please input your username')])
    password = PasswordField('密码', validators=[DataRequired(message='please input your password')])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登陆')


class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    password2 = PasswordField(
        '请重复一下您的密码', validators=[DataRequired(), EqualTo('password')])
    result = IntegerField('1+1=', validators=[DataRequired()])
    submit = SubmitField('注册')

    # 校验用户名是否重复
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('用户名重复，请重新输入')

    # 校验邮箱是否重复
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('邮箱重复，请重新输入')

    # 校验验证问题
    def validate_result(self, result):
        """这世界上只有10种人，懂二进制的和不懂的。"""
        if result.data != 10:
            raise ValidationError('结果错误，请重新计算')


class EditProfileForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(message="请输入用户名")])
    about_me = TextAreaField('关于我', validators=[Length(min=0, max=140)])
    submit = SubmitField('提交')


class ArticleForm(FlaskForm):
    author = StringField('作者', validators=[DataRequired(message="请输入作者")])
    title = StringField('标题', validators=[DataRequired(message="请输入标题")])
    article = TextAreaField('文章', validators=[Length(min=0, max=5000)])
    submit = SubmitField('发布')
