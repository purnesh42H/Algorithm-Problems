def rotateArray(a, k, n):
	n_index = 0
	k_index = 0
	while (k_index < k):
		n_index = 0
		last = a[n_index]
		while (n_index < n-1):
			a[n_index] = a[n_index+1]
			n_index += 1
		a[n] = last
		k_index += 1