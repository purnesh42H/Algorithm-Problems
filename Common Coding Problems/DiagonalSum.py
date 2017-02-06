#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
    
sumD1 = 0
sumD2 = 0
i = 0
j = n-1
while i < j:
    sumD1 += a[i][i] + a[j][j]
    sumD2 += a[i][j] + a[j][i]
    i += 1
    j -= 1
    
print abs(sumD1 - sumD2)
