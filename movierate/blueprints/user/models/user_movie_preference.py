from extensions import db
from .movie_model import Movie
from .util_sqlalchemy import ResourceMixin


class UserMoviePreference(db.Model, ResourceMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)

    movie_id = db.Column(db.Integer(), db.ForeignKey('movie.id'),
                         nullable=False)
    other_movie_id = db.Column(db.Integer(), db.ForeignKey('movie.id'))
    liked_more_than_the_other = db.Column(db.Boolean())

    movie = db.relationship(Movie, foreign_keys=[movie_id])
    other_movie = db.relationship(Movie, foreign_keys=[other_movie_id])

    # Only one record of user-movie 
    db.UniqueConstraint(user_id, movie_id, other_movie_id)

    def __init__(self, **kwargs):
        # Call Flask-SQLAlchemy's constructor.
        super().__init__(**kwargs)

