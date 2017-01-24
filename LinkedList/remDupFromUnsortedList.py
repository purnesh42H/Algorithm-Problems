class Node:

    def __init__(self, d):
        self.data = d
        self.next = None

    def insertWithTail(self, d):
        if self.next == None:
            self.next = Node(d)
            return self.next

# Key points/Assumptions:
'''
1. No extra buffer allowed
2. We don't what exist in the list
'''

# Algorithm:
'''
1. Keep 2 pointers (current and inner)
2. For each current pointer data, run inner pointer from head to current and
   if the current node data is found, skip the current node(cur.data = inn.next.data and cur.next = inn.next.next)
'''

# Code:

def remDup(head):
	cur = head.next
	prev = head
	
	while cur != None:
		inner = head
		while inner != cur:
			if cur.data == inner.data:
				prev.next  = cur.next
				break
			inner = inner.next
			
		if inner == cur:
			prev = cur
		cur = cur.next
		
	return head
	
	
# Test:
'''
[1,2,3,2,6] => [1,2,3,6]
'''

head = Node(1)
head.insertWithTail(2).insertWithTail(3).insertWithTail(2).insertWithTail(6).insertWithTail(6).insertWithTail(3)
            
