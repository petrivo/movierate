from app import db
from user_like_movie import UserLikesMovie


class User(db.Model):
    # __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    built_tree = db.Column(db.PickleType(), nullable=True)
    # Relationships
    user_likes_movie = db.relationship(UserLikesMovie, uselist=True,
                                       backref='user')

