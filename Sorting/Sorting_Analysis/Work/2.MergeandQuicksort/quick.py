import random



def insertion_sort(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_wrap(arr, low, high,threshold=10):
    """
    Sort the arr in place using quick sort algorithm. 
    In-place quick sort with Randomized pivot selection

    1. Optimize it with insertion sort for small subarr in our case its 10 and randomize the pivot selection.
    """
    

    if low < high:
        if high - low < threshold:
            insertion_sort(arr, low, high)
            print("insertion @",low,high)
        else:
             
            pivot = partition(arr, low, high)
            quick_sort_wrap(arr, low, pivot - 1)
            quick_sort_wrap(arr, pivot + 1, high)

length = random.randint(30, 50)
arr = [random.randint(0, 100) for _ in range(length)]

quick_sort_wrap(arr,0,length-1)
print(arr)

