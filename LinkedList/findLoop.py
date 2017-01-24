# Key Points/Assumptions:
'''
1. It can be any list(circular or non circular) and its singly link list
2. Node should be compared by reference not data
'''

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

    def insertWithTail(self, d):
        self.next = Node(d)
        return self.next
    
# Algorithm:
'''
1. keep two pointers. one twice as fast other
2. Move with their respective speeds unless you find end or both
   having same next node.
3. Previous to this found next node is your loop beginning node
'''

# Example:
'''
1. 1->3->5->6->3
         s     f
'''

# Code:
class Result:
    node = None
    isCircular = False

    def __init__(self, node, isCirc):
        self.node = node
        self.isCircular = isCirc


def loopDetect(head):
    slow = head
    fast = head

    while fast != None and fast.next != None and fast != slow:
        slow = slow.next
        fast = fast.next.next

    if fast == None or fast.next == None:
        return Result()

    slow = head
    while fast != slow:
        slow = cur.next
        fast = fast.next

    return Result(fast, True)

head1 = Node(9)
head1.insertWithTail(7).insertWithTail(8).insertWithTail(10).next = head1

#Tests:
'''
1. 9->7->8
      f  s
 
'''
