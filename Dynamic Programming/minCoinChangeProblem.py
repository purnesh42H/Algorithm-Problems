#!/usr/bin/env python

# To find the minimum number of coins required to change target T from the given
# set of coins D[1...k]. Assume that there is infinite pile of each coin.

# Subproblem: C[s] = minimum coins required to change s from coins 1..di where
#                    i <= k

# No. of subproblems: Tk

# Recursion: C[s] = 1 + min(C[s-di]) where i <= k

# Solution: C[T]

# Running time: O(Tk)

def findMinCoins(d, t):
    d.sort()
    k = d[-1]
    C = [99999 for i in xrange(t+1)]
    C[0] = 0
    L = [-1 for i in xrange(t+1)]
    for i in range(1, len(C), 1):
        for j in range(len(d)):
            if i - d[j] >= 0:
                min = 1 + C[i-d[j]]
                if C[i] > min:
                    C[i] = min
                    L[i] = max(j, L[i-d[j]])

    min = C[t]
    while t > 0:
        print d[L[t]]
        t = t - d[L[t]]

    return min, L

