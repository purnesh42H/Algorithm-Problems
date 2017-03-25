#!/usr/bin/env python

# Find the longest increasing subsequence of a given sequence S[1...n].

# Also output the subsequence

# Subproblem: LIS[i] = Longest subsequence of S[1..i]
#                      including the i-th character

# No. of subproblems: n

# Recursion: LIS[i] = 1 + max(LIS[j]) where j < i and S[j] < S[i]

# Solution: max(LIS)

# Running Time: n * O(n) = O(n^2)

def findLIS(s):
    LIS = [1 for i in range(len(s))]
    L = [-1 for i in range(len(s))]
    max, maxIndex = 0, 0
    for i in range(len(s)):
        max, maxIndex = 0, -1
        for j in range(i):
            if s[j] < s[i] and LIS[j] > max:
                max = LIS[j]
                maxIndex = j

        LIS[i] = 1 + max
        L[i] = maxIndex

    max, maxIndex = 1, 0
    for i, element in enumerate(LIS):
        if max < LIS[i]:
            max = element
            maxIndex = i

    output = []
    while maxIndex >= 0:
        output.append(s[maxIndex])
        maxIndex = L[maxIndex]

    return max, output[::-1]
