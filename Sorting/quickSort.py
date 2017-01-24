def quickSort(a, left, right):
	index = partition(a, left, right)
	if left < index - 1:
		quickSort(a, left, index - 1)
	if index < right:
		quickSort(a, index, right)

def partition(a, left, right):
	pivot = a[(left+right)/2]
	while left <= right:
		while a[left] < pivot:
			left += 1
		while a[right] > pivot:
			right -= 1
		if left <= right:
			swap(a, left, right)
			left += 1
			right -= 1

	return left

def swap(a, i, j):
	temp = a[i]
	a[i] = a[j]
	a[j] = temp
