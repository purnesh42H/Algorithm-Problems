#!/bin/python

import sys

for _ in range(int(raw_input().strip())):
    n, k = [int(x) for x in raw_input().strip().split(' ')]
    if k != 0 and n % k != 0:
        print(-1)
        continue

    arr = [None] * (n+1) # initialize iterable
    for i in range(1,len(arr)):
        if arr[i] is None:
            arr[i] = i + k
            arr[i+k] = i

    print(' '.join([str(j) for j in arr[1:]]))
