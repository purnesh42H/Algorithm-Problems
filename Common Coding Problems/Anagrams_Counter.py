from collections import *

def number_needed(a, b):
    a_dict = Counter(a)
    b_dict = Counter(b)
    a_dict.subtract(b_dict)
    delCount = 0
    
    for key, value in a_dict.items():
        delCount += abs(value)
    
    return delCount

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)