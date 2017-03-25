#!/usr/bin/env python

# Find the longest common subsequence of a given sequences S1[1...n] and S2[1..m]
# Also output the sequence

# Subproblem: LCS[i, j] = LCS of s1 and s2  upto upto i-th char of s1
#             and j-th char of s2

# No. of subproblems: m*n

# Recursion:
'''
if i = 0 or j = 0:
    LCS[i, j] = 0
elif s1[i-1] == s2[j-1]:
    LCS[i, j] = 1 + LCS[i-1, j-1]
else:
    LCS[i, j] = max(LCS[i-1, j], LCS[i, j-1])
'''

# Solution: L[m, n]

# Running Time: O(mn)

def findLCS(s1, s2):
    m = len(s1)
    n = len(s2)
    if m == 0 or n == 0:
        return 0
    
    LCS = [[0 for j in xrange(n+1)] for i in xrange(m+1)]
    for i in xrange(m+1):
        for j in xrange(n+1):
            if i == 0 or j == 0:
                LCS[i][j] = 0
            if s1[i-1] == s2[j-1]:
                LCS[i][j] = 1 + LCS[i-1][j-1]
            else:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

    i,j = m, n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            print s1[i-1]
            i -= 1
            j -= 1
            
        elif LCS[i-1][j] > LCS[i][j-1]:
            i -= 1
        else:
            j -= 1

    return LCS[m][n] - 1
            
    
