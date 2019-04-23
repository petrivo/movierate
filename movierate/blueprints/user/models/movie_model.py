from movierate.extensions import db
from movierate.blueprints.user.models.util_sqlalchemy import ResourceMixin

class Movie(db.Model, ResourceMixin):
    id = db.Column(db.Integer, primary_key=True)
    omdb_id = db.Column(db.String(20), unique=True, nullable=False)

    def __init__(self, **kwargs):
        # Call Flask-SQLAlchemy's constructor.
        super().__init__(**kwargs)
