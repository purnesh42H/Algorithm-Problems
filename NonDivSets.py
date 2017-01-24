# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import *

t = int(raw_input().strip())
for case in range(t):
    x, y = raw_input().strip().split(' ')
    x, y = [int(x), int(y)]
    sqrtx = int(ceil(sqrt(x)))
    sqrty = int(floor(sqrt(y)))
        
    print sqrty - sqrtx + 1
