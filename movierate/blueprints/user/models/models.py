from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from extensions import db
from .movie_model import Movie
from .user_movie_preference import UserMoviePreference
from .util_sqlalchemy import ResourceMixin


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
    user_movie_preference = db.relationship(UserMoviePreference, backref='user')

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

    # def generate_movie_comparison_list(self):
    #     user_movies = UserMoviePreference.query.with_entities(
    #         UserMoviePreference.movie_id).filter(
    #         UserMoviePreference.user_id == self.id)
    #     movies_without_preference = user_movies.filter(UserMoviePreference.
    #                                             other_movie_id == None).distinct().all()
    #     comp_list = []

    #     for e in movies_without_preference:
    #         movie = Movie.query.get(e[0])
    #         comp_list.append(movie)
        
    #     vs = []
    #     for i in range(len(comp_list)):
    #         curr = comp_list[i]
    #         for e in comp_list[i+1:]:  
    #             compare = [curr, e]
    #             vs.append(compare)

    #     self.comparing_list = vs
    #     db.session.commit()

    #     return vs

    def increase_seen_movies_count(self):
        self.seen_movies_count += 1
        db.session.commit()