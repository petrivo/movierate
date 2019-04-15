from extensions import db


class UserMoviePreference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    liked_more_than_the_other = db.Column(db.Boolean())
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)

    movie_id = db.Column(db.Integer(), db.ForeignKey('movie.id'),
                         nullable=False)
    other_movie_id = db.Column(db.Integer(), db.ForeignKey('movie.id'))

    movie = db.relationship("Movie", foreign_keys=[movie_id])
    other_movie = db.relationship("Movie", foreign_keys=[other_movie_id])
