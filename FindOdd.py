def findOdd(arr):
    nDict = {}
    n = len(arr)
    sumN = 0
    for i in range(n):
        if arr[i] in nDict:
            nDict[arr[i]] += 1
            sumN -= arr[i]
        else:
            nDict[arr[i]] = 1
            sumN += arr[i]

    return sumN


arr = [1,1,2,2,3]
print findOdd(arr)
