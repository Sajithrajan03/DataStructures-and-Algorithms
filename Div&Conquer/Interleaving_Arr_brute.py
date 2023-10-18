import math

def divide_and_interleave(arr, low,mid, high):
    if high - low < 2:
        return
    mid = low+ math.ceil((high-low)/2)
    hmid = low + math.ceil((mid - low) / 2)
    hfull = mid + math.ceil((high - low) / 2)
                                                                                                                                                                
    arr[low:hmid], arr[mid:hfull] = arr[mid:hfull], arr[low:hmid]
    print(hmid,hfull,arr)
    divide_and_interleave(arr, low, hmid, mid)
    divide_and_interleave(arr, mid, hfull, high)

# Example usage:
arr1 = [1, 2, 3, 4, 'a', 'b', 'c', 'd']
divide_and_interleave(arr1, 0, 4, 8)
print(arr1)  # Output: [1, 'a', 2, 'b', 3, 'c', 4, 'd']
