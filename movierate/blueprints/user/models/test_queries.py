from user_movie_preference import UserMoviePreference

user_id = 1

seen_movie_ids = UserMoviePreference.query.with_entities(
            UserMoviePreference.movie_id).filter(UserMoviePreference. \
                user_id == user_id, UserMoviePreference.other_movie_id == None). \
                    distinct().all()

print(seen_movie_ids)