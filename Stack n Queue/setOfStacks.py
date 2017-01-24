from stack import *

class NewStack(MyStack):

    def __init__(self, data):
        super(NewStack, self).__init__(data)
        self.elements = 1
        
    def push(self, item):
        super(NewStack, self).push(item)
        self.elements += 1

    def pop(self):
        item = super(NewStack, self).pop()
        if item != None:
            self.elements -= 1
        return item

    def peek(self):
        return super(NewStack, self).peek()

    def isEmpty(self):
        return self.elements == 0

    def length(self):
        return self.elements

class SetOfStacks:
    stacks = []
    threshold = 1

    def __init__(self, data, threshold = 1):
        self.stacks.append(NewStack(data))
        self.threshold = threshold

    def peek(self):
        if len(self.stacks) > 0:
            return self.stacks[-1].peek()

    def push(self, item):
        if len(self.stacks) > 0:
            if self.stacks[-1].length() == self.threshold:
                self.stacks.append(NewStack(item))
            else:
                self.stacks[-1].push(item)
        else:
            self.stacks.append(NewStack(item))

    def pop(self, index):
        if len(self.stacks) >= index:
            item = self.stacks[index-1].pop()
            if self.stacks[index-1].isEmpty():
                if index == len(self.stacks)
                    self.stacks = self.stacks[:-1]
            return item

        return None

    def pop(self):
        return self.pop(0)
    


# Tests:
'''
[[3 2], [5 4]]
'''
