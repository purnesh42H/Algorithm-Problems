# Example:
'''
            6
        7       8
     3       5
    6
   4
'''


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

    def isBalanced(self, left=0, right=0):
        if abs(left - right) > 1:
            return False

        if self.left != None:
            if self.right != None:
                return self.left.isBalanced(left+1,right+1)
            else:
                return self.left.isBalanced(left+1,right)
        if self.right != None:
            if self.left != None:
                return self.right.isBalanced(left+1,right+1)
            else:
                return self.right.isBalanced(left,right+1)

        return True 
    '''
    def isBalanced(self):
        return self.checkHeight() != -999

    def checkHeight(self):
        if self == None:
            return -1
        left = -1
        if self.left != None:
            left = self.left.checkHeight()
        if left == -999:
            return -999
        right = -1
        if self.right != None:
            right = self.right.checkHeight()
        if right == -999:
            return -999
        diff = abs(left - right)
        if diff > 1:
            return -999
        else:
            return max(left, right) + 1
    '''

bt = BTree(6)
#bt.insert(3)
bt.insert(8)
#bt.insert(2)
#bt.insert(4)
#bt.insert(7)
bt.insert(9)

