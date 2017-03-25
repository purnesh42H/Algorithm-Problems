# Subproblem: Total number of coins required to change c, where c <= t
# Total Subproblems: t
# Recursion: C[s, i] = C[s, i - 1] + C[s-d[i], i-1]
# Solution: C[t, n]
# Running time: t * O(n)[Time to solve each subproblem] = O(tn)

def changeCoins(t, d):
    n = len(d)
    C = [[0 for j in xrange(t+1)] for i in xrange(n)]
    for i in xrange(n):
        C[i][0] = 1
       
    for i in xrange(n):
        for c in xrange(1, t+1):
            if i - 1 >= 0:
                C[i][c] = C[i-1][c]
            if c - d[i] >= 0:
                C[i][c] += C[i][c-d[i]]
                 
    return C[n-1][t]

t, n = map(int, raw_input().strip().split(' '))
d = map(int, raw_input().strip().split(' '))
    
print changeCoins(4, [1 2 3])
