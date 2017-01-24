# Key Points:
'''
1. Maintain both head and tail(insert from tail and remove from head)
2. Check if queue is empty
3. Maintain some threshold here(stop the push after that)
'''

#Algorithm:
'''
1. Four methods, insert, delete, peek, isEmpty(tail is empty?)
2. Insert, create a node, make it tail.
3. Delete, remove head and make the next node as head
4. peek, return the head
5. isEmpty, if  tail is empty
'''

# Code:
class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data

class MyQueue:
    head = None
    tail = None

    def __init__(self, data):
        node = Node(data)
        self.insert(data)

    def insert(self, item):
        node = Node(item)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def delete(self):
        if not self.isEmpty():
            item = self.head.data
            self.head = self.head.next
            if self.head == None:
                self.tail = None
            return item

        return None

    def peek(self):
        if not self.isEmpty():
            return self.head.data

    def isEmpty(self):
        return self.head == None

# Tests:
'''
queue = MyQueue(2) => [2]
queue.push(3) => 2->3
queue.push(4) => 2->3->4
queue.delete() => 2, 3->4
queue.peek() => 3
'''
        
