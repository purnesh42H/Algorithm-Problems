def array_left_rotation(a, n, k):
    n_index = 0
    rot_a = []
    while n_index < n:
        rot_a.append(a[(n_index + k)%n])
        n_index += 1
        
    return rot_a
	