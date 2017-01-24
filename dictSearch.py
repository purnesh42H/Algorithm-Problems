#!/bin/python
from collections import *

import sys

def lonely_integer(a):
    dict = {}
    for num in a:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    lon = {k:v for k, v in dict.iteritems() if v == 1}
    return lon.keys()[0]

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a)
