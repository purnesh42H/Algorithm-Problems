from collections import *

class Node:

    def __init__(self, pid):
        self.pid = pid
        self.children = []
        self.dependencies = 0

    def incrDependencies(self):
        self.dependencies += 1

    def decrDependencies(self):
        self.dependencies -= 1
        
class Graph:
    
    def __init__(self, nodes, edges):
        self.nodes = {}
        self.create(nodes,edges)

    def create(self, nodes, edges):
        for node in nodes:
            self.nodes[node.pid] = node
                
        for edge in edges:
            self.nodes[edge[0].pid].children.append(edge[1])
            self.nodes[edge[1].pid].incrDependencies()

    def getGraph(self):
        return self.graph


# Example:
'''
{a:d, b:d, c: , d:c, f:a,b 
f->a->d->c
f->b->d->c
e

'''
def rootNodes(graph, buildOrder):
    for id in graph.nodes:
        if graph.nodes[id].dependencies == 0:
                buildOrder.append(graph.nodes[id])
            
def projectOrder(graph):
    buildOrder = []
    rootNodes(graph, buildOrder)

    cur = 0
    prevLen = len(buildOrder)
    print len(buildOrder)
    if len(buildOrder) == 0:
        return 'Error: Cycle detected'
    
    while len(buildOrder) != len(graph.nodes):
        current = buildOrder[0]

        childIndex = 0
        for child in graph.nodes[current.pid].children:
            if graph.nodes[child.pid].dependencies != 0:
                graph.nodes[child.pid].decrDependencies()

        rootNodes(graph, buildOrder)
        print len(buildOrder)
        cur += 1
        if cur == len(buildOrder):
            return 'Error: Cycle detected'

    return buildOrder
        

# Tests:
nodes = [Node('a'), Node('b'), Node('c'), Node('d'), Node('e'), Node('f')]
edges = [[Node('a'), Node('d')], [Node('f'), Node('b')], [Node('b'), Node('d')], [Node('f'), Node('a')], [Node('d'), Node('c')]]
