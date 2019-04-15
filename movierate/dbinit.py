from app import db
from user import User
from movie_model import Movie
from user_movie_preference import UserMoviePreference
from movie import Movie as Mov
from algo import Node
from sqlalchemy import update

db.drop_all()
db.create_all()

user1 = User(username="abc")
user2 = User(username="xyz")

movies = list("ABCDF")

for e in movies:
    mov = Movie(title=e)
    db.session.add(mov)
    db.session.commit()

usr_mov0 = UserMoviePreference(user_id=1, movie_id=1, other_movie_id=2,
                          liked_more_than_the_other=True)
usr_mov1 = UserMoviePreference(user_id=1, movie_id=1, other_movie_id=3,
                          liked_more_than_the_other=True)
usr_mov2 = UserMoviePreference(user_id=1, movie_id=1, other_movie_id=4,
                          liked_more_than_the_other=False)
usr_mov3 = UserMoviePreference(user_id=1, movie_id=1, other_movie_id=5,
                          liked_more_than_the_other=True)
usr_mov4 = UserMoviePreference(user_id=1, movie_id=2, other_movie_id=3,
                          liked_more_than_the_other=False)
usr_mov5 = UserMoviePreference(user_id=1, movie_id=2, other_movie_id=4,
                          liked_more_than_the_other=True)
usr_mov6 = UserMoviePreference(user_id=1, movie_id=2, other_movie_id=5,
                          liked_more_than_the_other=True)
usr_mov7 = UserMoviePreference(user_id=1, movie_id=3, other_movie_id=4,
                          liked_more_than_the_other=True)
usr_mov8 = UserMoviePreference(user_id=1, movie_id=3, other_movie_id=5,
                          liked_more_than_the_other=False)
usr_mov9 = UserMoviePreference(user_id=1, movie_id=4, other_movie_id=5,
                          liked_more_than_the_other=True)

db.session.add(user1)
db.session.add(user2)
db.session.add(usr_mov0)
db.session.add(usr_mov1)
db.session.add(usr_mov2)
db.session.add(usr_mov3)
db.session.add(usr_mov4)
db.session.add(usr_mov5)
db.session.add(usr_mov6)
db.session.add(usr_mov7)
db.session.add(usr_mov8)
db.session.add(usr_mov9)

db.session.commit()

user_preferences = UserMoviePreference.query.filter(UserMoviePreference.user_id == 1)

# print(user_preferences)
# print(user_preferences.all())

movie_objs = []

for pref in user_preferences:
    movie = Mov(pref.movie.title)
    other_movie = Mov(pref.other_movie.title)
    
    movie_obj = next((x for x in movie_objs if x.title == movie.title), None)
    other_movie_obj = next((x for x in movie_objs if x.title == other_movie.title), None)

    if movie_obj is None:
        movie_obj = Mov(movie.title)
        movie_objs.append(movie_obj)
    
    if other_movie_obj is None:
        other_movie_obj = Mov(other_movie.title)
        movie_objs.append(other_movie_obj)

    if pref.liked_more_than_the_other:
        movie_obj.like_more_than(other_movie_obj)
    else:
        other_movie_obj.like_more_than(movie_obj)

node = Node(movie_objs[0])

for obj in movie_objs[1:]:
    node.insert(obj)

# node.inorder()
# print(node.inorder_list)

# update(User).where(User.id == 1).values(built_tree=node.inorder_list)
user = User.query.get(1)
user.built_tree = node
db.session.commit()
