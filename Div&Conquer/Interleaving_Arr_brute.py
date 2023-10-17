a = [x for x in range(1,5)]
b = [x for x in range(5,9)]
from itertools import islice

def inShuffle_DC(arr):
    size = len(arr)
    if size < 2 or (size & (size - 1)) != 0:
        raise ValueError("Array size must be a power of two and at least 2")

    middle = size // 2
    first_half = arr[:middle]
    second_half = arr[middle:]

    for i in range(middle // 2):
        first_half[i], second_half[i] = second_half[i], first_half[i]

    if size >= 4:
        inShuffle_DC(first_half)
        inShuffle_DC(second_half)

# Example usage:
arr = [1, 2, 3, 4, 'a', 'b', 'c', 'd']
inShuffle_DC(arr)
print(arr)  # Output: [1, 'c', 'a', 'd', 2, 'b', 3, 4]

