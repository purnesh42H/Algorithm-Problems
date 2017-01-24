def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-2) + fibonacci(n-1)


def fibonacci2(n, fibs):
    if n <= 1:
        return n

    if n in fibs:
        return fibs[n]
    else:
        fibs[n] = fibonacci(n-1) + fibonacci(n-2)
        return fibs[n]


def fibonacci3(n):
    if n == 0:
        print n

    a = 0
    b = 1
    print a
    print b
    for i in range(2,n):
        c = a + b
        print c
        a = b
        b = c
