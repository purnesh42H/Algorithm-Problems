def longConsChain(a):
    curIndex = 0
    chainCount = 0
    maxIndexStart = 0
    maxIndexEnd = 0
    while curIndex < len(a) - 1:
        if a[curIndex] + 1 == a[curIndex+1]:
            chainCount += 1
        else:
            if chainCount > (maxIndexEnd - maxIndexStart):
                maxIndexStart = maxIndexEnd + 1
                maxIndexEnd = maxIndexStart + chainCount
            chainCount = 0

        curIndex += 1

    return maxIndexStart, maxIndexEnd


#1 2 3 5 6 7 8 10 11 12

