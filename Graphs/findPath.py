from queue import *

class Node(object):
    
    def __init__(self, id):
        self.id = id
        self.reachables = []

    def addReachable(self, node):
        if node not in self.reachables:
            self.reachables.append(node)

def hasPath_BFS(s, d):
    myQueue = MyQueue(s)
    visited = [s]
    found = False

    while not myQueue.isEmpty():
        node = myQueue.delete()
        for edge in node.reachables:
            if edge == d:
                found = True
                break
            if edge not in visited:
                visited.append(edge)
                myQueue.insert(edge)

    return found

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.addReachable(node2)
node2.addReachable(node3)
node3.addReachable(node4)

