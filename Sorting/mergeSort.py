def sort(a):
	helper = [None] * len(a)
	mergeSort(a, helper, 0, len(a) - 1)

def mergeSort(a, helper, left, right):
	if left < right:
		mid = (left + right)//2
		mergeSort(a, helper, left, mid)
		mergeSort(a, helper, mid + 1, right)
		merge(a, helper, left, mid, right)

def merge(a, helper, left, mid, right):
	i = left
	while i <= right:
		helper[i] = a[i]
		i += 1

	leftArray = left
	rightArray = mid + 1
	current = left

	while leftArray <= mid and rightArray <= right:
		if helper[leftArray] <= helper[rightArray]:
			a[current] = helper[leftArray]
			leftArray += 1
		else:
			a[current] = helper[rightArray]
			rightArray += 1
		current += 1

	remaining = mid - leftArray
	j = leftArray
	while j <= remaining:
		a[current + j] = helper[leftArray + j]
		j += 1
					

