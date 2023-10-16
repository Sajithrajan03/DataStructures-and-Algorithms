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

if __name__ == "__main__":
    arr_length = random.randint(10,20)
    arr = [chr(random.randrange(97,122)) for x in range(arr_length)]
    n = len(arr)
    print(f"Input: {arr}")
    print(f"Input length: {arr_length}")
    print(f"Output: {insertion_sort(arr,n)}")
    
