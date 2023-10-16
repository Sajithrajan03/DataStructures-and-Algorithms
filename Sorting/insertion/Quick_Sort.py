import random as r
def partition(arr, low, high):
	pivot = arr[high]
	i = low - 1
	for j in range(low, high):
		if arr[j] <= pivot:
			i = i + 1
			(arr[i], arr[j]) = (arr[j], arr[i])
		print(arr,i,j)
	(arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
	
	return i + 1

def quicksort(arr, low, high):
	if low < high:
		pi = partition(arr, low, high)
		quicksort(arr, low, pi - 1)
		quicksort(arr, pi + 1, high)

if __name__ == '__main__':
	length = r.randint(10,20)
	arr = [(r.randrange(0,20)) for x in range(length)]
	print('Unsorted arr:')
	print(arr)
	N = len(arr)
	quicksort(arr, 0, N - 1)
	print('Sorted arr:')
	print(arr)


