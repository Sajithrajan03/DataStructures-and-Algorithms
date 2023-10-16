import random as r
def partition(arr,low,high):
    pivot = arr[high]
     
    j = low-1
    for i in range(low,high):
        if arr[i]<=pivot:
            j+=1
            arr[j],arr[i]= arr[i],arr[j]
    arr[j+1],arr[high] = arr[high],arr[j+1]
    return j+1
def quick(arr,low,high):
    if (low<high):
        p = partition(arr,low,high)
        quick(arr,low,p-1)
        quick(arr,p+1,high)

if __name__ == '__main__':
	length = r.randint(10,20)
	arr = [(r.randrange(0,20)) for x in range(length)]
	print('Unsorted arr:')
	print(arr)
	N = len(arr)
	quick(arr, 0, N - 1)
	print('Sorted arr:')
	print(arr)


