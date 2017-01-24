# Key points/Assumptions:
'''
1. Are all ascii chars? - Yes
2. Are they c-style string? - No
3. What about equal strings? - Zero edit
'''

# Algorithm:
'''
1. Create dictionaries of both strings with key as char and value as frequency.
2. Subtract both dictionaries.
3. If resultant dictionary has only one element left with frequency of 1
   one edit distance away
'''

# Examples:
'''
1. pale, ple => {p:1,a:1,l:1,e:1} - {p:1,l:1,e:1} = {a:1} - True
2. pale, bake = > {p:1,a:1,l:1,e:1} - {b:1,a:1,k:1,e:1} = {b:1,k:1} - False
'''

# Code
# Using counter from collections:

from collections import *

def isOneAway(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    
    counter1 = Counter(s1)
    counter2 = Counter(s2)

    if len(s1) >= len(s2):
        res = counter1 - counter2
    else:
        res = counter2 - counter1
    if len(res) != 1 or res.values()[0] != 1:
        return False
    return True

def isOneWay2(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False

    if len(s1) == len(s2):
        return checkReplace(s1, s2)
    else:
        return checkInsert(s1, s2)

def checkReplace(s1, s2):
    notFound = 0
    i = 0
    while i < len(s1) and notFound <= 1:
        if s1[i] != s2[i]:
            notFound += 1
        i+=1

    return notFound == 1

def checkInsert(s1, s2):
    if len(s2) > len(s1):
        temp = s1
        s1 = s2
        s2 = temp

    i = 0
    j = 0
    notFound = 0
    while i < len(s1) and j < len(s2) and notFound <= 1:
        if s1[i] != s2[i]:
            notFound += 1
            j += 1
        else:
            i+=1
            j+=1

    return notFound <= 1

#Tests:
'''
1. pales, pale => {p:1,a:1,l:1,e:1, s:1} - {p:1,a:1,l:1,e:1} => {s:1} => True
'''

# Problems/Trade-offs/Improvements:
'''
1. Two operations doing O(s1) and O(s2)
2. Subtracting dictionary -> O(n)
'''
