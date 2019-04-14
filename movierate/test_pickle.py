from user import User
from movie_model import Movie


node = User.query.get(1).built_tree

# node.inorder()
print(type(node))
data = []
node.inorder(data)

# print(data)

for m in data:
    print(m.title)