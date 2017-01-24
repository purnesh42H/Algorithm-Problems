class Heap:
    lst = []

    def parentIndex(childIndex):
        (childIndex - 1)/2

    def leftChildIndex(parentIndex):
        parentIndex * 2 + 1

    def rightChildIndex(parentIndex):
        parentIndex*2 + 1

    def hasParent(index):
        return index >= 0

    def hasLeftChild(index):
        return leftChildIndex(index) < len(lst)

    def hasRightChild(index):
        return rightChildIndex(index) < len(lst)

    def swap(index1, index2):
        temp = lst[index1]
        lst[index1] = lst[index2]
        lst[index2] = temp

    def heapifyDown():
        index = 0
        left = leftChildIndex(index)
        right = rightChildIndex(index)
    
        while hasLeftChild(index) and (lst[index] > lst[left] or lst[index] > lst[right]) :
            if (lst[left] < lst[right]):
                swap(index, left)
                index = left
            else:
                swap(index, right)
                index = right
            left = leftChildIndex(index)
            right = rightChildIndex(index)

    def heapifyUp():
        index = len(lst) - 1
        parentIndex = getParentIndex(index)
        while hasParent(index) and lst[index] > lst[parentIndex]:
            swap(index, parentIndex)
            index = parentIndex
            
    def peek():
        if len(lst) != 0:
            return lst[0]
        else:
            return None

    def delete():
        if len(lst) == 0:
            print 'No element to delete'
            return
        lst[0] = lst[-1]
        lst = lst[:-1]
        heapifyDown()

    def insert(value):
        lst.append(value)
        heapifyUp()
        
