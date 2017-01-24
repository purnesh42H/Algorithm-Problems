#!/bin/python

import sys


a,b,c,d,e = raw_input().strip().split(' ')
arr = [int(a),int(b),int(c),int(d),int(e)]
sortA = sorted(arr)

sumMin = 0
sumMax = 0

for num in range(len(sortA) - 1):
    sumMin += sortA[num]
    sumMax += sortA[-num - 1]
    
print '%d %d' % (sumMin, sumMax)
