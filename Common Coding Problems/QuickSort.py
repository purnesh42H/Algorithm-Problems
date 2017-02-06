arr = [2,3,55,6,1,9,8,7,9,7,8,7] 

def quickSort():
    quickSortRec(arr, 0, len(arr) - 1)

def quickSortRec(a, left, right):
    if left != right:
        pivot = (left+right)/2
        partI = partition(a, left, right, pivot)
        quickSortRec(a, left, partI-1)
        quickSortRec(a, partI, right)
 
def partition(a, left, right, pivot):
    while left < right:
        while a[left] < a[pivot]:
            left += 1

        while a[right] > a[pivot]:
            right -= 1

        if left <= right:
            temp = a[left]
            a[left] = a[right]
            a[right] = temp
            left +=1
            right -= 1

    return left

quickSort()
print arr
        
    
