from movie import Movie


class Node():

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            elif data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
        else:
            self.data = data

    def inorder(self, in_list):
        if self.left:
            self.left.inorder(in_list)
        # print(self.data)
        in_list.append(self.data)
        if self.right:
            self.right.inorder(in_list)


# a = Movie('A')
# b = Movie('B')
# d = Movie('D')
# c = Movie('C')
# f = Movie('F')


# a.like_more_than(b)
# a.like_more_than(c)
# d.like_more_than(a)
# a.like_more_than(f)
# c.like_more_than(b)
# b.like_more_than(d)
# b.like_more_than(f)
# c.like_more_than(d)
# f.like_more_than(c)
# d.like_more_than(f)

# node = Node(a)
# node.insert(b)
# node.insert(c)
# node.insert(d)
# node.insert(f)

# node.inorder()
