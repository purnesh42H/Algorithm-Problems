# Enter your code here. Read input from STDIN. Print output to STDOUT
def reverse(num):
    rev = 0
    while num > 0:
        rev = (10*rev) + num%10
        num //= 10
    return rev

i, j, k = raw_input().strip().split(' ')
i, j, k = [int(i), int(j), int(k)]
bD = 0
while i <= j:
    rev = reverse(i)
    if abs(rev - i) % k == 0:
        bD += 1
    i = i+1
    
print bD
