found = False
last = None

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
                
    def findInOrdSuc(self, node):
        self.findInOrdSuc2(node, next)

    def findInOrdSuc2(self, node, next):
        global last
        global found
        
        if self == None:
            return
        
        if self.left != None:
            if last == None:
                if found:
                    last = self
                    self.left.findInOrdSuc2(node, self)
                else:
                    self.left.findInOrdSuc2(node, last)

        if self.data == node.data:
            found = True

        if self.right != None:
            if last == None:
                if found:
                    last = self
                    self.right.findInOrdSuc2(node, self)
                else:
                    self.right.findInOrdSuc2(node, last)

        return

bt = BTree(6)
bt.insert(3)
bt.insert(8)
bt.insert(2)
bt.insert(4)
bt.insert(7)
bt.insert(9)
