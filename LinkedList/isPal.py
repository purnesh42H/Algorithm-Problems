class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

    def insertWithTail(self, d):
        self.next = Node(d)
        return self.next

# Key Points/Assumptions:
'''
1. Length of the list is not known
2. Singly link list
3. List can contain anything
   (if it contains only chars we can use a boolean array of 26)
'''

# Algorithm:
'''
1. Logic is to match the first half of the list with second half.
2. store the first half in a stack and compare the values from stack
   with second half.
3. If length of list is known, stop at middle, else use two pointers,
   one twice as fast as other.
4. once the fast pointer reaches last of list, first pointer would have reached
   middle.
'''

#Example
'''
1. [1,2,3,4,3,2,1] => Palindrome
'''

# Code
def isPal(head):
    slow = head
    fast = head

    stack = []
    while fast != None and fast.next != None:
        fast = fast.next.next
        stack.append(slow.data)
        slow = slow.next

    if fast != None:
        slow = slow.next

    while slow != None:
        val = stack.pop()
        if slow.data != val:
            return False
        slow = slow.next

    return True

head1 = Node(9)
head1.insertWithTail(7).insertWithTail(9)
