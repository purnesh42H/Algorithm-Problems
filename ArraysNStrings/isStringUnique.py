# Key points/assumpotions:
'''
1. Does string has all ascii chars? coz otherwise we will need more storage
- Yes
2. Is string a cstlye string? so that I can ignore the last char
- No
'''

# Algorithm:
'''
1. keep track of each character and mark them true as they appear.
2. If any character already marked true, appears again return false.
3. Also, if string length is more than 256, return false as there cannot be more than 256 unique ascii chars
'''

# Code:
def isUnique(s):
    if len(s) > 256:
        return False
    chars = [False]*256
    for c in s:
        if chars[ord(c)]:
            return False
        chars[ord(c)] = True

    return True

# Test:
'''
1. s = 'abvd' - Unique
2. s = 'fgthyuih' - Not unique
'''

# Bottlenecks:
'''
1. Space complexity is O(c) where c = 256
2. Time complexity is O(n) where n = length of s
'''

# Special case:
# If all chars are small letters a-z, we can bring down the space complexity
# by using a bit vector

def isUnique2(s):
    checker = 0
    for c in s:
        val = ord(c)- ord('a')
        check = checker & 1<<val
        if check > 0:
            return False
        checker |= 1<<val

    return True
