class Node:

    def __init__(self, d):
        self.data = d
        self.next = None

    def insertWithTail(self, d):
        if self.next == None:
            self.next = Node(d)
            return self.next

# Key Points/Assumptions:
'''
1. All elements less than or equal to partition must come
   left to it(not necessarily sorted)
2. Right partition need not to be sorted
3. Partition can come anywhere at right(if its present)
4. The elements are integers
'''

# Algorithm:
'''
1. Store all elements <= partition in a list and rest in an another list.
2. Create a new list by keeping the first array elemens before elements of other array.
'''

# Optimized Algorithm:
'''
1. Create a new list by inserting left partition at head and right partition at tail.
'''

# Code:
def partition(head, x):
    newHead = head
    newTail = head

    while head != None:
        node = Node(head.data)
        if head.data < x:
            node.next = newHead
            newHead = node
        else:
            node.next = None
            newTail.next = node
            newTail = node

        head = head.next

    newTail.next = None
    return newHead

# Tests:
'''
1. [3, 5, 8, 5, 10, 2, 1], x = 5 => 1->2->3->5->8->5->10
'''

head = Node(1)
head.insertWithTail(2).insertWithTail(3).insertWithTail(2).insertWithTail(6).insertWithTail(6).insertWithTail(3)

head = partition(head, 3)
while head != None:
    print head.data
    head = head.next
