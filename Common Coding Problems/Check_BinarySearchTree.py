from collections import *

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def inOrderList(root, oDict):
    if root.left != None:
        inOrderList(root.left, oDict)
    
    if root.data in oDict:
        oDict[root.data] += 1
    else:
        oDict[root.data] = 1
        
    if root.right != None:
        inOrderList(root.right, oDict)
    
    return oDict

def check_no_duplicates(oDict):
    return any((oDict[x] > 1 for x in oDict))
    
def sortDict(oDict):
    return (OrderedDict (sorted(oDict.items(), key=lambda x : x[0])))
    
def check_inorder(oDict):
    return (not check_no_duplicates(oDict)) and oDict == sortDict(oDict)

def check_binary_search_tree_(root):
    return check_inorder(inOrderList(root, OrderedDict()))