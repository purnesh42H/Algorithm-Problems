class Node:
	
	def __init__(data):
		self.data = data
		self.node = None

def revList(head):
	if head == None or head.next == None:
		return head
	newHead = head
	cur = head.next
	while cur != None:
		node = Node(cur.data)
		node.next = newHead
		newHead = node
		cur = cur.next

	return newHead
		
		
	