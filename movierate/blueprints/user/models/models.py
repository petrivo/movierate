from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from extensions import db
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
    
    # Relationships
    user_movie_preference = db.relationship(UserMoviePreference, backref='user')

    # Activity tracking
    sign_in_count = db.Column(db.Integer, nullable=False, default=0)

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