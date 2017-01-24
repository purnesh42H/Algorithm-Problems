def findMax(arr):
    low = 0
    high = len(arr) - 1
    mid = (low + high)//2
    while low < high and arr[mid] <= a[mid + 1]:
        if a[mid] >= a[mid-1]:
            low = mid + 1
        elif a[mid] <= a[mid-1]:
            high = mid - 1

        mid = (low + high) // 2

    return a[mid]


# Example:
# 4 5 6 7 8 9 1 2 3

def revString(s):
    rev = revList(list(s))
    return ''.join(e for e in rev)

def revList(lst):
    if len(lst) < 2:
        return lst
    return revList(lst[1:]) + [lst[0]]
        
