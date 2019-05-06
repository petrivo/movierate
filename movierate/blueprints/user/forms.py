from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import Email, DataRequired, Length, EqualTo
from wtforms_alchemy import Unique, ModelForm
from movierate.blueprints.user.models.user import db, User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired(), Length(2, 150)])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 64)])
    remember_me = BooleanField('Remember me')


class RegisterForm(FlaskForm, ModelForm):
    email = StringField('Email', validators=[
        Email(),
        DataRequired(),
        Length(2, 150),
        Unique(User.email, get_session=lambda: db.session)])
    password = PasswordField('Password', validators=[
        Length(6, 64, "At least 6 characters long"),
        DataRequired(),
        EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')