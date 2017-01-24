def has_cycle(head):
    if not head:
        return 0
    
    nodeDict = {}
    current  = head
    while current.next:
        if current.data in nodeDict:
            return 1
        nodeDict[current.data] = 1
        current = current.next
    
    return 0