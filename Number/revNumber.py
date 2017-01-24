def revNumber(num):
    rev = 0
    while num > 0:
        rev = rev*10 + num%10
        num = num/10

    return rev

def binarySearch(a, num):
    start = 0
    end = len(a) - 1
    while start < end:
        mid = (start + end)/2
        if a[mid] == num:
            return True
        elif num < a[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return False
        
