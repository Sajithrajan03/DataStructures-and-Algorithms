def subsequence(ind,arr,ans,n):
    if ind == n:
        print(ans)
        return 
    ans.append(arr[ind])
    subsequence(ind+1,arr,ans,n)
    ans.pop()
    subsequence(ind+1,arr,ans,n)
    
arr = [1,2,3]
subsequence(0,arr,[],3)
    
    