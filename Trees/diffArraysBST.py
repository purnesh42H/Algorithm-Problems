class Node:

    data = None
    right = None
    left = None

    def __init__(self, data):
        self.data = data

    def insert(self, data):
        if self == None:
            return
        if data < self.data:
            if self.left != None:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right != None:
                self.right.insert(data)
            else:
                self.right = Node(data)


    def preorder(self, out):
        if self == None:
            return
        
        out.append(self.data)
        
        if self.left != None:
            self.left.preorder(out)

        if self.right != None:
            self.right.preorder(out)

    def inorder(self, out):
        if self == None:
            return
        
        if self.left != None:
            self.left.inorder(out)

        out.append(self.data)

        if self.right != None:
            self.right.inorder(out)

            
bt = Node(5)
bt.insert(3)
bt.insert(8)
bt.insert(1)
bt.insert(4)
bt.insert(6)
bt.insert(9)
bt.insert(2)
        
        
            
