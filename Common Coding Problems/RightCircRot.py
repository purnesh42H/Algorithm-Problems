#!/bin/python

import sys


n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))

rotA = a[n-k:] + a[:n-k]
for a0 in xrange(q):
    m = int(raw_input().strip())
    print rotA[m]
