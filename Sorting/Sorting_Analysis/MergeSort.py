def mergesort(arr,low,high):
    if low<high:
        mid = (low+high)//2
        mergesort(arr,low,mid)
        mergesort(arr,mid+1,high)
        merge(arr,low,mid,high)
def merge(arr,low,mid,high):
    temp = list()
    left = low
    right = mid+1
    while(left<=mid and right<=high):
        if arr[left]<arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while(left<=mid):
        temp.append(arr[left])
        left+=1
    while(right<=high):
        temp.append(arr[right])
        right+=1
    for i in range(low,high+1):
        arr[i] = temp[i-low]


import random
a = [(random.randrange(1,20)) for _ in range(0,10)]
print(a)
mergesort(a,0,len(a)-1)
print(a)


