class Node():

    def __init__(self, data=None):
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
