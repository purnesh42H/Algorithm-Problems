def reverse(cs):
    cList = list(cs)
    revList = []
    while cList:
        revList.append(cList.pop())

    return ''.join(ch for ch in revList)


def reverse2(cs):
    org = cs[:-1]
    return org[::-1] + cs[-1]

def reverse3(cs):
    return reverse(cs[:-1]) + cs[-1]
