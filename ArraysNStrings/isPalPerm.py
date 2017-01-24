# Key Points/Assumptions:
'''
1. Are all ascii chars? - Yes
2. C-style string? - No
'''

# Algorithm:
'''
1. Count the occurence of each char in string.2
2. If lenght of string(excluding spaces) is even
    all chars should have same freq
   else
    all chars should have same freq except one
'''

# Examples:
'''
1. 'abc'-odd;all have same - False
2. 'abba'-even; all have same- True
3. 'abcba'-odd;all have same except c - True
4. 'abccba' - even; all have same - True
5. 'aaabbbcbbbaaa' - odd; all have same except one  - True
6. 'aaabbbcbbbaaad' - even; not all have same - False
7. 'aaabbbcbbbaaaddde' - odd; two have different - False
'''

#code:

def getCounter(s):
    chars = [0] * 256
    for c in s:
        chars[ord(c)] += 1

    return chars

def oddPerm(s, counter):
    falseCount = 0
    i = 0
    while i < len(s):
        if counter[i] % 2 != 0:
            falseCount += 1
        if falseCount > 2:
            return False
        i += 1

    return (False if falseCount > 1 else True)

def isPalPossible(s):
    if len(s) < 3:
        return True

    s = s.replace(' ','').lower()
    counter = getCounter(s)
    
    return oddPerm(s, counter)

# Tests:
'''
1. s = 'Taco Coa'; counter{t:1,a:2,c:2,o:2} => acotoca
2. s = 'Bbrrcc'; counter{b:2,r:2,c:2} => brccrb
'''

#Problems/bottlenects/Improvements:
'''
1. We can improve oddPerm and evenPerm(combine them)
2. counter is taking space complexity of O(c) = O(256)
3. Time complexity is O(n)
'''

    
