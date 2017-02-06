"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def SortedInsert(head, data):
    if head == None:
        head = Node(data)
        return head
    
    if data < head.data:
        newNode = Node(data)
        newNode.next = head
        head.prev = newNode
        return newNode
   
    cur = head.next
    prev = head
    
    while cur != None:
        if data < cur.data:
            newNode = Node(data)
            newNode.next = cur
            newNode.prev = prev
            cur.prev = newNode
            prev.next = newNode
            return head
        prev = cur
        cur = cur.next
        
    newNode = Node(data)
    newNode.prev = cur
    prev.next = newNode
    
    return head
