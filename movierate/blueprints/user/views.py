from flask import Blueprint, render_template, request, url_for, redirect, flash
from .forms import LoginForm
from .models.models import User
from flask_login import (
    login_required,
    login_user,
    current_user,
    logout_user)

user = Blueprint('user', __name__, template_folder='templates')

@user.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    flash("flash message")

    if form.validate_on_submit():
        user = User.find_by_email(email=request.form.get('email'))

        if user and user.authenticated(password=request.form.get('password')):
            flash('user password is:{0}'.format(user.password))
            if login_user(user):
                return redirect(url_for('user.dashboard'))

    return render_template('user/login.html', form=form)


@user.route('/dashboard')
@login_required
def dashboard():
    return render_template('user/dashboard.html')