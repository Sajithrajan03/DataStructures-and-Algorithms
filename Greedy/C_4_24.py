import random

def quick_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    
    groups = [arr[i:i+5] for i in range(0, len(arr), 5)]

    
    medians = [sorted(group)[len(group)//2] for group in groups]
    pivot = quick_select(medians, len(medians)//2)

    
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    if k < len(left):
        return quick_select(left, k)
    elif k < len(left) + len(equal):
        return equal[0]
    else:
        return quick_select(right, k - len(left) - len(equal))

 
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
b = arr
b.sort()
print(b)
k = 5  
result = quick_select(arr, k)
print(f"The {k+1}th smallest element is: {result}")
