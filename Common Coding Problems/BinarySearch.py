from collections import *

def subArr(a, m, n):
    i = n - 1
    while i  > 0:
        if m > a[i]:
            return a[:i+1]
        i-=1
  
    return a

def findFlavours(a, dict, m):
    left = 0
    right = len(a) - 1
    cost = a[left] + a[right]
    while left < right and cost != m:
        if cost <= m:
            left += 1
        else:
            right -= 1
        cost = a[left] + a[right]
        
    return  a[left], a[right]
    

t = int(raw_input().strip())
for a0 in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    dict = OrderedDict()
    for i in range(n):
        if a[i] in dict:
            dict[a[i]].append(i)
        else:
            dict[a[i]] = [i]
    a, b = findFlavours(subArr(sorted(a),m, n), dict, m)
    if a == b:
        print '%d %d' % (dict[a][0]+1, dict[a][1]+1)
    else:
        m1 = min(dict[a][0]+1, dict[b][0]+1)
        m2 = max(dict[a][0]+1, dict[b][0]+1)
        print '%d %d' % (m1, m2)
