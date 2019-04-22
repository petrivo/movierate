from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, PasswordField
from wtforms.validators import Email, DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired(), Length(2, 150)])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 64)])


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired(), Length(2, 150)])
    password = PasswordField('Password', [DataRequired(),
        EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')