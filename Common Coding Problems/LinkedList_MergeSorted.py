"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def MergeLists(headA, headB):
    if headA == None:
        return headB
    elif headB == None:
        return headA
    
    next = None
    head = None
    
    while headA != None and headB != None:
        if headA.data < headB.data:
            newNode = headA
            headA = headA.next
        else:
            newNode = headB
            headB = headB.next
            
        if head == None:
            head = newNode
        elif head.next == None:
            head.next = newNode
        else:
            next.next = newNode
        
        next = newNode
        
    while headA != None:
        newNode = headA
        next.next = newNode
        next = newNode
        headA = headA.next
    
    while headB != None:
        newNode = headB
        next.next = newNode
        next = newNode
        headB = headB.next
        
    next.next = None
    return head
