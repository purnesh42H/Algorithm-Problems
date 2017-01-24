class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

    def insertWithTail(self, d):
        self.next = Node(d)
        return self.next

# Key Points?Assumptions:
'''
1. Linked lists are not of same length
2. Output should also be reversed
'''

# Algorithm:
'''
1. Follow simple addition approach starting from unit digits and passing on the carry.
2. Add the carry subsequent addtions
3. Add the remaining element from the longer list to the output list
'''

# Example:
'''
6->2 + 3->5->6 => 9->7->6
'''

# Code:
def add(l1, l2):
    if l2 == None:
        return l1
    elif l1 == None:
        return l2

    return addSub(l1, l2, 0)



def addSub(l1, l2, carry):
    if l1 == None and l2 == None:
        if carry == 0:
            return None
        else:
            sum = carry
    elif l1 == None:
        sum = l2.data + carry
        l2 = l2.next
    elif l2 == None:
        sum = l1.data + carry
        l1 = l1.next
    else:
        sum = l1.data + l2.data + carry
        l1 = l1.next
        l2 = l2.next
        
    if sum > 9:
        node = Node(sum%10)
        node.next = addSub(l1, l2, 1)
    else:
        node = Node(sum)
        node.next = addSub(l1, l2, 0)

    return node

class PartSum:
    node = None
    carry = 0

def addForward(l1, l2):
    n1 = length(l1)
    n2 = length(l2)

    if n1 < n2:
        l1 = pad0(l1,n2-n1)
    else:
        l2 = pad0(l2,n1-n2)

    res = addListHelper(l1, l2)
    print res.node.data
    print res.carry
    if res.carry == 0:
        return res.node
    else:
        return insertBefore(res.node, res.carry)


def pad0(lst, num):
    i = 0
    for i in range(num):
        lst = insertBefore(lst, 0)

    return lst


def insertBefore(head, d):
    new = Node(d)
    if head != None:
        new.next = head

    return new

def length(lst):
    i = 0
    while lst != None:
        i += 1
        lst = lst.next

    return i

def addListHelper(l1, l2):
    if l1 == None and l2 == None:
        return PartSum()

    sum = addListHelper(l1.next, l2.next)
    if sum.node != None:
        print sum.node.data
    print sum.carry
    val = sum.carry + l1.data + l2.data

    res = insertBefore(sum.node, val%10)

    sum.node = res
    sum.carry = val/10
    return sum

head1 = Node(9)
head1.insertWithTail(7).insertWithTail(8)

head2 = Node(6)
head2.insertWithTail(8).insertWithTail(5)
            

        
