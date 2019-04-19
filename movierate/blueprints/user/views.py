from flask import Blueprint, render_template, request, url_for, redirect, flash, session
from .forms import LoginForm
import sqlalchemy
from .models.models import User
from .models.movie_model import Movie
from .models.user_movie_preference import UserMoviePreference
from flask_login import (
    login_required,
    login_user,
    logout_user,
    current_user,
    logout_user)
import sys

user = Blueprint('user', __name__, template_folder='templates')


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
    if request.method == 'POST':
        # print('posted', file=sys.stderr)
        print(request.get_json())
        print(request.get_json()['movie_id'])

    # TODO display inorder if possible

    return render_template('user/dashboard.html')


@user.route('/add_movie', methods=['POST'])
@login_required
def add_movie():
    omdb_id = request.get_json()['movie_id']
    inserted = UserMoviePreference.add_seen_movie(omdb_id, current_user.id)

    # if inserted: TODO check contition
    current_user.increase_seen_movies_count()

    return inserted

@user.route('/compare')
@login_required
def compare():
    # TODO has to be generated or rebuilt one time an later just used
    current_user.generate_movie_comparison_list()
    compare_two = current_user.comparing_list[-1]
    flash(compare_two)
    return render_template('user/compare.html', data=compare_two)


@user.route('/preferred_movie', methods=['POST'])
@login_required
def preferred():
    movie_won = request.get_json()['movie_id']

    competing_movies = current_user.comparing_list.pop()
    print(competing_movies)
    movie = competing_movies[0]
    other_movie = competing_movies[1]

    if movie.omdb_id == movie_von:
        pass
    
    if movie[movie_von]:
        pass 

    pass