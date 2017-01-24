#!/bin/python

import sys
from math import *

s = raw_input().strip()
l = len(s)
rootL = sqrt(l)
floorL = floor(rootL)
ceilL = ceil(rootL)
if ceilL == floorL:
    ceilL = ceilL + float(1.0)

r = floorL
c = floorL
    
col = False
while r*c < l:
    if col:
        r = ceilL
    else:
        c = ceilL
        col = True

encode = []
i = 0
while i < l:
    encode.append(list(s[i:i+int(c)]))
    i += int(c)

i = 0
j = 0
encodedStr = ''
while j < c:
    i = 0
    while i < r:
        if j < len(encode[i]):
            encodedStr += encode[i][j]
        i += 1
    j+= 1
    encodedStr += ' '
    
print encodedStr
