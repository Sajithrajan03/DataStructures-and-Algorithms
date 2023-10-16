import random
def insertion_sort(arr,n):
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(f"Pass {i}: {arr}")
    return arr


# arr_length = random.randint(10,20)
# arr = [random.randrange(0,100) for x in range(arr_length)]
arr = [10,20,4,4,6]
print(f"Input: {arr}")
for i in range(len(arr) - 1, -1, -1):
    if arr[i] % 10 == 0:
        arr.pop(i)
print(arr)
# print(f"Input length: {arr_length}")
# print(f"Output: {insertion_sort(arr,n)}")

