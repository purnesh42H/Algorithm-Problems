
# Code
class BTree:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left == None:
                self.left = BTree(data)
            else:
                self.left.insert(data)
        else:
            if self.right == None:
                self.right = BTree(data)
            else:
                self.right.insert(data)

    def isBST(self, minVal = None, maxVal = None):
        if self == None:
            return True
        
        if (minVal != None and self.data <= minVal) or (maxVal != None and self.data > maxVal):
            return False

        if self.left != None:
            return self.left.isBST(minVal, self.data)
        if self.right != None:
            return self.right.isBST(self.data, maxVal)

        return True

bt = BTree(6)
bt.insert(3)
bt.insert(8)
bt.insert(2)
bt.insert(4)
bt.insert(7)
bt.insert(9)        
