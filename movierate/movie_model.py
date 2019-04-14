from app import db
from user_like_movie import UserLikesMovie


class Movie(db.Model):
    # __tablename__ = 'movie' 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    