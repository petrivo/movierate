from flask import Blueprint, render_template, request, url_for, redirect, flash
from movierate.blueprints.user.forms import LoginForm, RegisterForm
from movierate.blueprints.user.models.models import User
from movierate.blueprints.user.models.user_movie_preference import UserMoviePreference
from flask_login import login_required, login_user, current_user, logout_user
import json

user = Blueprint('user', __name__, template_folder='templates')


@user.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('You are already signed in')
        return redirect(url_for('user.dashboard'))

    form = RegisterForm()

    if form.validate_on_submit():
        print('form validated')
        email = request.form.get('email')
        password = request.form.get('password')

        user = User(email=email, password=password)
        user.save()
        print(user)
        login_user(user)

        flash('welcome to the movierate')
        return redirect(url_for('user.dashboard'))

    return render_template('user/register.html', form=form)


@user.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already signed in')
        return redirect(url_for('user.dashboard'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.find_by_email(email=request.form.get('email'))

        if user and user.authenticated(password=request.form.get('password')):
            flash('user password is:{0}'.format(user.password))
            if login_user(user):
                return redirect(url_for('user.dashboard'))

    return render_template('user/login.html', form=form)


@user.route('/signout')
@login_required
def signout():
    logout_user()
    flash('You have been signed out')
    return redirect(url_for('user.login'))


@user.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    bst = current_user.update_tree()
    in_list = []
    if bst:
        bst.inorder(in_list)
        in_list = [x.title for x in in_list]
    print(in_list)
    return render_template('user/dashboard.html', data=json.dumps(in_list))


@user.route('/add_movie', methods=['POST'])
@login_required
def add_movie():
    omdb_id = request.get_json()['movie_id']
    # if inserted: TODO check contition
    current_user.increase_seen_movies_count()

    inserted = UserMoviePreference.add_seen_movie(omdb_id, current_user.id)
    return inserted


@user.route('/compare')
@login_required
def compare():
    compare_two = UserMoviePreference.get_compare_for_user(current_user.id)
    if not compare_two:
        flash('You have compared all your movies')
        return redirect(url_for('user.dashboard'))
        
    flash(compare_two)
    return render_template('user/compare.html', data=compare_two)


@user.route('/preferred_movie', methods=['POST'])
@login_required
def preferred():
    _id = int(request.get_json()['database_id'])
    like_more_than_other = bool(int(request.get_json()['preferred']))
    print(_id, like_more_than_other)
    UserMoviePreference.update(_id, like_more_than_other)
    
    return 'ajax success'