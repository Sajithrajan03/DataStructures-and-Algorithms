import random

def quick_sort(arr, k):
    

    pivot = random.choice(arr)
    less = []
    equal = []
    greater = []

    for x in arr:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    if k <= len(less):
        return quick_sort(less, k)
    elif k <= len(less) + len(equal):
        return pivot
    else:
        return quick_sort(greater, k - len(less) - len(equal))

N = int(input())
for _ in range(N):
    A = list(map(int, input().split()))
    B = int(input())
    result = quick_sort(A, B)
    print("{}, {}".format(result, A.index(result)))