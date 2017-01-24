from stack import *

def sortStack(stack):
    item = stack.pop()
    stack2 = MyStack(item)
    buffer = False
    
    while stack.top != None:
        if not buffer:
            item = stack.pop()
            buffer = True
        if stack2.peek() != None:
            if item > stack2.peek():
                stack.push(stack2.pop())
            else:
              buffer = False
              stack2.push(item)  
        else:
            buffer = False
            stack2.push(item)
        

    return stack2

# Tests:
'''
[4 2 1 3 6 7]  => []
'''

stack1 = MyStack(4)
stack1.push(2)
stack1.push(1)
stack1.push(3)
stack1.push(6)
stack1.push(7)
stack1.push(11)
stack1.push(2)
stack1.push(6)
stack1.push(9)
stack1.push(10)

stack2 = sortStack(stack1)

while stack2.peek() != None:
    print stack2.pop()
