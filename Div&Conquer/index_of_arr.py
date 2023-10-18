def divide(arr, low, high):
    global arr_index
    if low <= high:
        mid = (low + high) // 2
        k = arr_index
        # print(low,mid,high,arr[low:high+1],arr_index)
        if arr[mid] == mid:
            if arr_index>mid:
                arr_index = mid
        if k==arr_index:
            divide(arr, low, mid - 1)
            divide(arr, mid + 1, high)
        elif arr[mid]>=mid:
            divide(arr, low, mid - 1)
        elif arr[mid]<=mid:
            divide(arr, mid + 1, high)
        
    return arr_index

test = int(input())
 
for _ in range(test):
    
    a = list(map(int, input().split()))
    arr_index = len(a)
    er = divide(a, 0, len(a) - 1)
    
    if a[0] == 0:
        print(f"True, 0")
    elif arr_index==len(a):
        print("False, -1")
    else:
        print(f"True, {er}")
