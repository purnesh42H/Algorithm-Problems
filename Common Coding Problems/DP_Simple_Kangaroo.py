#!/bin/python

# https://www.hackerrank.com/challenges/kangaroo

import sys


x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

meets = False


faster = x1
vf = v1
slower = x2
vs = v2
if v1 < v2:
    faster = x2
    vf = v2
    slower = x1
    vs = v1
    
while v1!=v2 and faster <= slower:
    if faster == slower:
        meets = True
        break
    else:
        faster += vf
        slower += vs
        
if meets:
    print 'YES'
else:
    print 'NO'
