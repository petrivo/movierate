from extensions import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    omdb_id = db.Column(db.String(20), unique=True, nullable=False)
