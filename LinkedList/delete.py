class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

    def insertWithTail(self, d):
        self.next = Node(d)
        return self.next

    def delete(self, n):
        if n.next == None or n == None:
            return False
        
        n.data = n.next.data
        n.next = n.next.next
        return True
        

head = Node(1)
head.insertWithTail(2).insertWithTail(3).insertWithTail(4).insertWithTail(5).insertWithTail(6).insertWithTail(3)
