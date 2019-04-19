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

    # Only one record of user-movie comparison
    db.UniqueConstraint(user_id, movie_id, other_movie_id)

    def __init__(self, **kwargs):
        # Call Flask-SQLAlchemy's constructor.
        super().__init__(**kwargs)

    @classmethod
    def add_seen_movie(cls, omdb_id, user_id):
        movie = Movie.query.filter(Movie.omdb_id == omdb_id).first()

        if not movie:
            movie = Movie(omdb_id=omdb_id)
            movie.save()

        params = {
            'user_id': user_id,
            'movie_id': movie.id,
        }

        usr_mov = UserMoviePreference(**params)
        inserted = False
        last_id = None
        # TODO should return json for ajax
        # TODO ? move it to general resource mixin?
        try:
            usr_mov.save()
            inserted = True
            last_id = usr_mov.id
        except sqlalchemy.exc.SQLAlchemyError as err:
            print(err)

        # logic for automatic generation rows for comparison list
        seen_movie_ids = UserMoviePreference.query.with_entities(
            UserMoviePreference.id, UserMoviePreference.movie_id).filter(
                UserMoviePreference.user_id == user_id, 
                UserMoviePreference.liked_more_than_the_other == None). \
                    distinct().all()

        print(seen_movie_ids)

        if inserted and len(seen_movie_ids) == 2:
            # compare first to second and second to first
            # Potential problems of having two comparisons? or maybe create
            #   fiction movie for this case?
            preference1 = UserMoviePreference.query.get(seen_movie_ids[0][0])
            preference2 = UserMoviePreference.query.get(seen_movie_ids[1][0])

            preference1.other_movie_id = seen_movie_ids[1][1]
            preference2.other_movie_id = seen_movie_ids[0][1]

            db.session.commit()

        if inserted and len(seen_movie_ids) > 2:
            last_insertion = UserMoviePreference.query.get(seen_movie_ids[-1][0])
            last_insertion.other_movie_id = seen_movie_ids[0][1]

            # !problem is in here see print statement after third insertion
            other_movies = set(x for x in seen_movie_ids[1:-1][1])
            print(other_movies)
            for e in other_movies:
                # other_movie_id = UserMoviePreference.query.get(e[0]).movie_id
                other_movie_id = e
                params = {
                    'user_id': user_id,
                    'movie_id': last_insertion.movie_id,
                    'other_movie_id': other_movie_id
                }
                usr_mov = UserMoviePreference(**params)
                usr_mov.save()

        return 'to be translated to json'
