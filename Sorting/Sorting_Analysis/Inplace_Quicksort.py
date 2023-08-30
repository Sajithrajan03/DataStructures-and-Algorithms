import random
import time
import matplotlib.pyplot as plt

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def analyze_time(input_sizes):
    execution_times = []

    for size in input_sizes:
        arr = [random.randint(1, 100) for i in range(size)]

        start_time = time.time()
        quick_sort(arr, 0, len(arr) - 1)
        end_time = time.time()

        execution_times.append(end_time - start_time)

    return execution_times

input_sizes = [100, 500, 1000, 2000, 5000,10000]
execution_times = analyze_time(input_sizes)

plt.plot(input_sizes, execution_times, marker='o',markersize=14)
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('In-place Quick Sort Performance')
plt.grid(True)
plt.show()
