class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

    def insertWithTail(self, d):
        self.next = Node(d)
        return self.next

    def nToLast(self, n):
        cur = self
        stack = []
        while cur != None:
            stack.append(cur.data)
            cur = cur.next
        i = 0
        element = 0
        while stack and i < n:
            element = stack.pop()
            i += 1

        if i == n:
            return element

        return None

    def nToLast2(self, n):
        cur = self
        arr = []
        while cur != None:
            arr.append(cur.data)
            cur = cur.next

        if n <= len(arr):
            return arr[-n]

        return None

    def nToLast3(self, n):
        if n < 1 or self == None:
            return None
        p1 = self
        p2 = self

        i = 0
        while i < n:
            if p2 == None:
                return None
            p2 = p2.next
            i += 1

        while p2.next != None:
            p1 = p1.next
            p2 = p2.next

        return p1

    def nToLast4(self, n):
        head = self
        return self.nToLast(head, n)

    def nToLast(head, cur, n):
        if cur == None:
            return None if n > 0 else head

        if n > 0:
            return head.nToLast(cur.next,n-1)
        else:
            return head.next.nToLast(cur.next,0)

# Key points/Assumptions:
'''
1. Not allowed to keep extra buffer
'''

# Algorithm:
'''
1. Keep two pointers.
2. Move one pointer to the nth element from first
3. Increment both pointer by 1 till the above pointer reaches end of the list
4. At this time, the current pointer will be the nth element of the node
'''

# Code:
def nthFromLast(head, n):
    cur = head
    other = head
    i = 0
    while i < n and other != None:
        other = other.next
        i += 1

    if i < n:
        return None

    while other != None:
        cur = cur.next
        other = other.next

    return cur.data


# Tests:
'''
1. [2,3,4,5,6], 2 =>
 other => 3
 At last => cur.data = 4 => 2nd element from last
'''

head = Node(1)
head.insertWithTail(2).insertWithTail(3).insertWithTail(4).insertWithTail(5).insertWithTail(6).insertWithTail(3)
