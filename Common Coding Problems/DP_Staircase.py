def paths(n):
    s0, s1, s2 = 1, 1, 2
    for _ in range(n):
        s0, s1, s2 = s1, s2, s0 + s1 + s2
    return s0

s = int(raw_input().strip())
for a0 in xrange(s):
    n = int(raw_input().strip())
    print paths(n)
