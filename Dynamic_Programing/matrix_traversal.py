def matrix_ways(m,n,memo):
    key = str(m)+','+str(n)
    if m==1 and n==1:
        return 1
    if m==0 or n==0:
        return 0
    if key in memo:
        return memo[key]
    memo[key] = matrix_ways(m-1,n,memo) + matrix_ways(m,n-1,memo)
    return memo[key]

print(matrix_ways(3,3,{}))
print(matrix_ways(4,2,{}))