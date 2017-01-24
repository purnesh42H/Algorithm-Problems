# Step 1: Questions
'''
4. Is it right rotated or left rotated? or I have to check for both?
5. Both strings are always of equal length?
6. Can I assume that both strings have same chars in same frequency?
'''

# Step 2: Algorithm
'''
1. If both strings are equal it means its a rotation of
   string 1 by len of string times.
2. If lenght both strings are different then return false
3. combine s2 with itself and check if s1 is substring of combination
'''

def isRotated(s1, s2):
    if len(s1) != len(s2):
        return False
    s2 = s2 + s2
    if s1 in s2:
        return True

    return False
