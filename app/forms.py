from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from bin.app.models import User


class LoginForm(FlaskForm):
    username = StringField('user_name', validators=[DataRequired(message='please input your username')])
    password = PasswordField('password', validators=[DataRequired(message='please input your password')])
    remember_me = BooleanField('remember me')
    submit = SubmitField('login')


class RegistrationForm(FlaskForm):
    username = StringField('user_name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    password2 = PasswordField(
        'Please repeat your password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('registration')

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
