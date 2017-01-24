#Example:
'''
[11 10 6] [6]
'''

from stack import *

class MinStack(MyStack):
    minStack = None

    def __init__(self, data):
        super(MinStack, self).__init__(data)
        self.minStack = MyStack(data)

    def push(self, item):
        super(MinStack, self).push(item)
        if self.minStack.isEmpty() or item <= self.minStack.peek():
            self.minStack.push(item)

    def pop(self):
        item = super(MinStack, self).pop()
        if item == self.minStack.peek():
            return self.minStack.pop()

        return item

    def min(self):
        return self.minStack.peek()
