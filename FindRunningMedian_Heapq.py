#!/bin/python

import sys
import heapq

def addNum(num,lowers,highers):
    if (not lowers) or (-num > lowers[0]):
        heapq.heappush(lowers,-num)
    else:
        heapq.heappush(highers,num)

def rebalance(lowers,highers):
    bigger = lowers if (len(lowers) > len(highers)) else highers
    smaller = highers if (len(lowers) > len(highers)) else lowers
    if len(bigger) - len(smaller) >= 2:
        heapq.heappush(smaller, -heapq.heappop(bigger))

def getMedian(lowers,highers):
    bigger = lowers if (len(lowers) > len(highers)) else highers
    smaller = highers if (len(lowers) > len(highers)) else lowers
    if len(bigger) > len(smaller):
        return abs(bigger[0])
    else:
        return (float(abs(bigger[0]) + abs(smaller[0])) / 2)

n = int(raw_input().strip())
a = []
a_i = 0
highers = []
lowers = []
for a_i in xrange(n):
    a_t = int(raw_input().strip())
    #a.append(a_t)
    addNum(a_t,lowers,highers)
    print lowers
    print highers
    rebalance(lowers,highers)
    print lowers
    print highers
    print round(getMedian(lowers,highers),1)