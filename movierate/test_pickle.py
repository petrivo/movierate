from user import User

node = User.query.get(1).built_tree

# node.inorder()
print(type(node))
data = []
node.inorder(data)

# print(data)

for m in data:
    print(m.title)