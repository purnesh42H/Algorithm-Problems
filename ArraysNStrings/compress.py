# Key Points/Assumptions:
'''
1. Only a-z letters
2. No c-style string
'''

# Algorithm:
'''
1. Create an array of size 26 to maintain count of each character
2. Append the count with charater and return the string
3. If freq of all values is 1, return original string
'''

# Code:
def compress(s):
    if len(s) <= 1:
        return s

    lst = []
    prev = s[0]
    count = 1
    i = 1
    while i < len(s):
        if s[i] == prev:
            count += 1
        else:
            lst.append(prev)
            lst.append(str(count))
            prev = s[i]
            count = 1

        i += 1

    lst.append(prev)
    lst.append(str(count))
    return ''.join(ch for ch in lst) if len(lst) < len(s) else s

# Example:
'''
1. 'abcfghy' => all has 1 freq, so hasRep = False, return s
2. 'abccccd' => abc4d
'''
