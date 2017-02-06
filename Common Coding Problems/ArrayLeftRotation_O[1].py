def array_left_rotation(a, n, k):
    rot_a = a[k:] + a[:k]
    return rot_a
   
n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))