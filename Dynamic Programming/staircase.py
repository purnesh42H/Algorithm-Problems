def stairs(n):
    a = [1, 2, 4]
    for i in range(0, n-3):
        a.append(a[-1] + a[-2] + a[-3])
    return a[-1]

def stairs1(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    return stairs1(n-3) + stairs1(n-2) + stairs1(n-1)


def stairs2(n):
    memo = [-1]*(n+1)
    return stairsSub(memo, n)

def stairsSub(memo, n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if memo[n] <= -1:
        memo[n] = stairsSub(memo, n-3) + stairsSub(memo, n-2) + stairsSub(memo, n-1)
        return memo[n]
    else:
        return memo[n]


def fibo(n):
    if n == 0:
        return 0
    a = 0
    b = 1
    for i in range(2, n):
        c = a + b
        print c
        a = b
        b = c

    return a + b
        
