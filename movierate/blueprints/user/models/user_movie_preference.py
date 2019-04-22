from extensions import db
from .movie_model import Movie
from .util_sqlalchemy import ResourceMixin
import sqlalchemy


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
    def get_compare_for_user(cls, user_id):
        compare_two = UserMoviePreference.query.filter(
            UserMoviePreference.user_id == user_id,
            UserMoviePreference.liked_more_than_the_other == None).first()
        
        if compare_two is None:
            return False
            
        return [compare_two.id, compare_two.movie, compare_two.other_movie]

    @classmethod
    def update(cls, _id, liked_more):
        pref = UserMoviePreference.query.get(_id)
        print(pref)
        pref.liked_more_than_the_other = liked_more
        db.session.commit()
        print(pref.liked_more_than_the_other)

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
        # TODO should return json for ajax
        # TODO ? move it to general resource mixin?
        try:
            usr_mov.save()
            inserted = True
        except sqlalchemy.exc.SQLAlchemyError as err:
            print(err)
        user = usr_mov.user
        # logic for automatic generation rows for comparison list
        seen_movie_ids = UserMoviePreference.query.with_entities(
            UserMoviePreference.id, UserMoviePreference.movie_id).filter(
                UserMoviePreference.user_id == user_id).distinct().all()
                # UserMoviePreference.liked_more_than_the_other == None). \
                    

        print(seen_movie_ids)

        if inserted and user.seen_movies_count == 2:
            # compare first to second and second to first
            # Potential problems of having two comparisons? or maybe create
            #   fiction movie for this case?
            preference1 = UserMoviePreference.query.get(seen_movie_ids[0][0])
            preference2 = UserMoviePreference.query.get(seen_movie_ids[1][0])

            preference1.other_movie_id = seen_movie_ids[1][1]
            preference2.other_movie_id = seen_movie_ids[0][1]

            db.session.commit()

        if inserted and user.seen_movies_count > 2:
            last_insertion = UserMoviePreference.query.get(seen_movie_ids[-1][0])
            last_insertion.other_movie_id = seen_movie_ids[0][1]

            sn_m = set(x[1] for x in seen_movie_ids[1:-1])
            print(sn_m)
            for e in sn_m:
                other_movie_id = e
                params = {
                    'user_id': user_id,
                    'movie_id': last_insertion.movie_id,
                    'other_movie_id': other_movie_id
                }
                usr_mov = UserMoviePreference(**params)

                # TODO check if bulk_save is more efficient
                usr_mov.save()

        return 'to be translated to json'
