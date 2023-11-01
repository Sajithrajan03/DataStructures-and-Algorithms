def matrix_chain_bottom_up(p):
    n = len(p) - 1
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for chain_length in range(2, n+1):
        for i in range(1, n - chain_length + 2):
            j = i + chain_length - 1
            dp[i-1][j-1] = float('inf')
            for k in range(i, j):
                cost = dp[i-1][k-1] + dp[k][j-1] + p[i-1] * p[k] * p[j]
                if cost < dp[i-1][j-1]:
                    dp[i-1][j-1] = cost

    return dp[0][n-1]


print(matrix_chain_bottom_up([1,2,3,4,3]))