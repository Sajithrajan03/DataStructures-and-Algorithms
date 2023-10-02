import random
def insertionsort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while(j>=0 and arr[j]>key):
            arr[j+1] =  arr[j]
            j -=1
        arr[j+1] = key
a = [(random.randrange(1,20)) for _ in range(0,10)]
print(a)
insertionsort(a)
print(a)