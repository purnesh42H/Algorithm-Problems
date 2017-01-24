def permute(s):
	allPerms(list(s), 0, len(s) - 1)

def allPerms(s, start, end):
	if start == end:
		print ''.join(c for c in s)
	i = start
	while i <= end:
		swap(s, i, start)
		allPerms(s, start + 1, end)
		swap(s, start, i)
		i += 1

def swap(s, i, j):
	temp = s[i]
	s[i] = s[j]
	s[j] = temp
	