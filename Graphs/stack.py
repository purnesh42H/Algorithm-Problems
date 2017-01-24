# Key Points:
'''
1. we always should know the top of stack(removal and insertion is o(1))
2. When stack is empty(no pop allowed)
3. sometimes once threshold is reached you won't allow anyomore insertions.
   You might create a new stack or you replace the top etc.
'''

# Algorithm:
'''
1. Four methods - push, pop, peek, isEmpty
2. For push, insert at top and return the top
3. For pop, remove top and decrement
4. peek, return top
5. isEmpty, if top is null
'''

# Code:
class MyStack(object):
    top = None

    def __init__(self, data):
        self.top = Node(data)

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.isEmpty():
            item = self.top.data
            self.top = self.top.next
            return item
        
        return None

    def peek(self):
        if not self.isEmpty():
            return self.top.data

        return None

    def isEmpty(self):
        return self.top == None

class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data

# Tests
'''
new = MyStack(2) => [2]
new.push(3) => 3 -> 2
new.push(4) => 4 -> 3 -> 2

new.pop() => 3->2, 4 as result
new.peek() => 3
'''
        
