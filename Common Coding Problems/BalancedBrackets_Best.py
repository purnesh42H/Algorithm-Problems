def is_matched(expression):
    stack = []
    for char in expression:
        if char == '{':
            stack.append('}')
        elif char == '[':
            stack.append(']')
        elif char == '(':
            stack.append(')')
        else:
            if len(stack) == 0 or char != stack.pop():
                return False
        
    return len(stack) == 0
            

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"