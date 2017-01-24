def powerSet(a):
    i = 1
    power = []
    while i <= len(a):
        subArrays(a,i,power)
        i += 1

    power.append([])
    return power


def subArrays(a, i, power):
    n = 0
    while n < len(a):
        new = a[n:n+i]
        if new not in power:
            power.append(new)
        n += 1

# [1,2]
  
            
        
