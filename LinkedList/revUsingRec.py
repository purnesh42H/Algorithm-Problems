class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data

    def insertTail(self,node):
        if head == None:
            head = node
            return head

        cur.next = node
        return cur


def reverse(head):
    node = None
    return revList(head, node)


def revList(head, node):
     if head == None or head.next == None:
        return head

     if node == None:
         node = revList(head.next, node)
     else:
         node.insertTail(revList(head.next, node))

def revIter(head):
    if head == None or head.next == None:
        return head

    cur = head
    while cur != None:
        node = Node(cur.data)
        node.next = head
        head = node
        cur = cur.next

    return head
         
n = Node(4)
n.next = Node(5)
n.next.next = Node(6)
    
