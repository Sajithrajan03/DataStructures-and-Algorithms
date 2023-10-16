def merge(arr,low,high):
    if  low<high:
        mid = (low+high)//2
        merge(arr,low,mid)
        merge(arr,mid+1,high)
        merge_sort(arr,low,mid,high)

def merge_sort(arr,low,mid,high):
    i = low
    j=mid+1
    temp = []
    
    while(i<=mid and j<=high):
        if arr[i]<=arr[j]:
            temp.append(arr[i])
            i +=1
        else:
            temp.append(arr[j])
            j +=1
    while i<=mid:
        temp.append(arr[i])
        i +=1
    while j<=high:
        temp.append(arr[j])
        j +=1
    print(low,mid,high,temp)
    for i in range(low,high+1):
        arr[i] = temp[i-low]

arr = [1,3,2,4,5,6,7,8,9,10]
merge(arr,0,len(arr)-1)