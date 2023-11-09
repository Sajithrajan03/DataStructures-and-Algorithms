def merge(arr,low,high):
    if high>low:
        mid=  (low+high)//2
        merge(arr,low,mid)
        merge(arr,mid+1,high)
        merge_sort(arr,low,mid,high)
    
def merge_sort(arr,low,mid,high):
    i = low
    j = mid+1
    temp = []
    while i<=mid and j<=high:
        if arr[i]>arr[j]:
            temp.append(arr[j])
            j +=1
        else:
            temp.append(arr[i])
            i +=1
    while i<=mid:
        temp.append(arr[i])
        i +=1
    while j<=high:
        temp.append(arr[j])
        j +=1
    for i in range(low,high+1):
        arr[i] = temp[i-low]
    
arr = [1,2,60,3,14,0,90,12]
merge(arr,0,len(arr)-1)
print(arr)