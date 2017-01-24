class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left == None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right == None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def preorder2(self):
        depths = []
        self.preorder(depths, 0)
        return depths

    def preorder(self, depths, nodes):
        if self == None:
            return
        
        if len(depths) == nodes:
            depths.append([self])
        else:
            depths[-1].append(self)

        if self.left != None:
            self.left.preorder(depths, nodes + 1)
        if self.right != None:
            self.right.preorder(depths, nodes + 1)

#Tests:
'''
'''

bt = Node(5)
bt.insert(4)
bt.insert(6)
bt.insert(3)
bt.insert(2)
