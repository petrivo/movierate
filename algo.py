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

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

node = Node(12)
node.insert(2)
node.insert(13)
node.insert(3)
node.insert(432)

node.inorder()