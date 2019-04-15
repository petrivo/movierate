from flask_wtf import Form
from wtforms import StringField, HiddenField, PasswordField
from wtforms.validators import Email, DataRequired, Length


class LoginForm(Form):
    email = StringField('Email', validators=[Email(), DataRequired(), Length(2, 150)])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 64)])