class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

    def insertWithTail(self, d):
        self.next = Node(d)
        return self.next

# Key Points/Assumptions:
'''
1. Lengths are not same
2. Singly lists
'''

# Algorithm:
'''
1. Brute force
2. Pick the first node from 1st list and search in another list
3. If found intersection is there else not.
'''

# Example:
'''
1. 1->2->3->4
              => 7->8->9
   4->5->6
'''

def findIntersection(head1, head2):
    cur1 = head1
    
    while cur1 != None:
        cur2 = head2
        while cur2 != None:
            if cur2 == cur1:
                return cur1
            cur2 = cur2.next

        cur1 = cur1.next

    return None

head1 = Node(9)
tail = head1.insertWithTail(7).insertWithTail(9)

head2 = Node(8)
head2.insertWithTail(10).insertWithTail(8).insertWithTail(1123).next = tail

tail.insertWithTail(7).insertWithTail(9)
