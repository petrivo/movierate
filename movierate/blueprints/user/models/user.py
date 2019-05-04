from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from movierate.extensions import db
from movierate.blueprints.user.models.movie_model import Movie
from movierate.blueprints.user.models.user_movie_preference import UserMoviePreference
from movierate.blueprints.user.models.util_sqlalchemy import ResourceMixin
from movierate.algo import Node
from movierate.movie import Movie as Mov


class User(UserMixin, ResourceMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Authentication
    username = db.Column(db.String(20), unique=True, index=True)
    email = db.Column(db.String(150), unique=True, nullable=False,
                      server_default='', index=True)
    password = db.Column(db.String(128), unique=False, nullable=False,
                         server_default='')
    active = db.Column('is_active', db.Boolean(), nullable=False,
                       server_default='1')

    # BST for movies that have been rated
    built_tree = db.Column(db.PickleType())
    comparing_list = db.Column(db.PickleType())

    # Relationships
    user_movie_preference = db.relationship(
        UserMoviePreference, backref='user')

    # Activity tracking
    sign_in_count = db.Column(db.Integer, nullable=False, default=0)
    seen_movies_count = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, **kwargs):
        # Call Flask-SQLAlchemy's constructor.
        super().__init__(**kwargs)
        self.password = User.encrypt_password(kwargs.get('password', ''))

    @classmethod
    def encrypt_password(cls, plaintext_password):
        if plaintext_password:
            return generate_password_hash(plaintext_password)

        return None

    @classmethod
    def find_by_email(cls, email):
        return User.query.filter(User.email == email).first()

    def authenticated(self, password):
        return check_password_hash(self.password, password)

    def increase_seen_movies_count(self):
        self.seen_movies_count += 1
        db.session.commit()

    def update_tree(self):
        user_preferences = self.user_movie_preference

        if len(user_preferences) == 0:
            return False

        movie_objs = []

        for pref in user_preferences:
            movie = Mov(pref.movie.omdb_id)
            other_movie = Mov(pref.other_movie.omdb_id)

            movie_obj = next(
                (x for x in movie_objs if x.title == movie.title), None)
            other_movie_obj = next(
                (x for x in movie_objs if x.title == other_movie.title), None)

            if movie_obj is None:
                movie_obj = Mov(movie.title)
                movie_objs.append(movie_obj)

            if other_movie_obj is None:
                other_movie_obj = Mov(other_movie.title)
                movie_objs.append(other_movie_obj)

            if pref.liked_more_than_the_other:
                movie_obj.like_more_than(other_movie_obj)
            else:
                other_movie_obj.like_more_than(movie_obj)

        node = Node()

        for obj in movie_objs:
            node.insert(obj)

        self.built_tree = node
        db.session.commit()

        return node
