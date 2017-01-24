class BTree:
    left = None
    right = None
    data = None

    def __init__(self, data):
        self.data = data

    def isValidBtree(self):
        lst = []
        return self.hasDupOrValid(lst)


    def hasDupOrValid(self, lst):
        print self.data
        if self.left != None:
            if self.data > self.left.data and self.data < self.right.data:
                return self.left.hasDupOrValid(lst)
            else:
                return False

        if len(lst) == 0 or (self.data not in lst and lst[-1] < self.data):
            lst.append(self.data)
        else:
            return False

        if self.right != None:
            if self.data > self.left.data and self.data < self.right.data:
                return self.right.hasDupOrValid(lst)
            else:
                return False
        
        return True
        
bt = BTree(5)
bt.left = BTree(4)
bt.right = BTree(6)
bt.left.right = BTree(7)
bt.left.left = BTree(5)
bt.right.right = BTree(8)
bt.right.left = BTree(2)
print bt.isValidBtree()
