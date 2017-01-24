# Key points/Assumptions:
'''
1. Are both strings ascii? - Yes
2. Are they c-style strings? - No
'''

# Algorithm:
'''
1. Store the counts of each char in the first string in an array
2. Traverse the second string and decrease the character count as they appear from
   the above array.
3. If none of the decrement result less than 0, first string is a perm of second
'''

'''
1. Create dictionaries of both strings
2. Subtract the dictionaries. The result should be empty if one is a perm of another
3. Also, they should be of same length
'''

# Example:
'''
s1 = 'abcd' s2='aabc' - False
'''

# code:
def isPerm(s1, s2):
    if len(s1) != len(s2):
        return False

    chars = [0] * 256
    for c in s1:
        chars[ord(c)] += 1

    for c in s2:
        chars[ord(c)] -= 1
        if chars[ord(c)] < 0:
            return False

    return True

# Tests:
'''
1. s1 = 'cfhgb', s2 = 'cfghb'
'''

# Problems/trade-offs:
'''
1. Less readable
'''

# A more flexible code.
# Use dictionary/counter

from collections import *

def isPerm2(s1, s2):
    counter1 = Counter(s1)
    counter2 = Counter(s2)
    return (counter1 - counter2) == {}
