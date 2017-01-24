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

    def subCountInOrd(self, m, n, count):
        if self.left != None:
            self.left.subCountInOrd(m, n, count)

        if self.data >= n:
            return count
        elif self.data > m:
            count.append(self.data)
        
        if self.right != None:
            self.right.subCountInOrd(m, n, count)

        return count
        

    def countSubTrees(self, m, n):
        return len(self.subCountInOrd(m, n, []))
        

bt = Node(6)
bt.insert(2)
bt.insert(4)
bt.insert(1)
bt.insert(5)

print bt.countSubTrees(2,6)
