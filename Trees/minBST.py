#Example:
'''
[1,2,3,4,5,6]
       3
    2     5
1            6
'''

class Node:
    data = None
    

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def createMinBST(array):
    return createSubMinBST(array, 0, len(array) - 1)


def createSubMinBST(array, start, end):
    if end < start:
        return None

    mid = (start + end)/2
    n = Node(array[mid])
    n.left = createSubMinBST(array, start, mid-1)
    n.right = createSubMinBST(array, mid+1, end)
    return n
