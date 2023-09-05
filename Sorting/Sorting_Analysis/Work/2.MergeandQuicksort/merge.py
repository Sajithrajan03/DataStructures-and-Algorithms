def merge(A, p, q, r):
    size_low = q - p + 1
    size_high = r - q

    low = [0] * (size_low + 1)
    high = [0] * (size_high + 1)

    for i in range(size_low):
        low[i] = A[p + i]

    for j in range(size_high):
        high[j] = A[q + j + 1]

    low[size_low] = float("inf")
    high[size_high] = float("inf")

    i = 0
    j = 0

    for k in range(p, r + 1):
        if low[i] <= high[j]:
            A[k] = low[i]
            i += 1

        else:
            A[k] = high[j]
            j += 1


def insertion_sort(array, low, high):
    for i in range(low + 1, high + 1):
        key = array[i]
        j = i - 1
        while j >= low and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def merge_sort(array, low, high, threshold=10):
    
    #Sort the array in place using merge sort algorithm.

   #Optimized with insertion sort for small subarrays.
  
     
    if low < high:
        if high - low < threshold:
            insertion_sort(array, low, high)
        else:
            mid = (low + high) // 2
            merge_sort(array, low, mid)
            merge_sort(array, mid + 1, high)
            merge(array, low, mid, high)