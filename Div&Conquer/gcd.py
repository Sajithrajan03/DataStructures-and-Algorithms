import math

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

def minimum_sum_after_operations(T, test_cases):
    results = []

    for t in range(T):
        X, Y, K = test_cases[t]
        gcdval = gcd(X, Y)
        lcmval = lcm(X, Y)

        if K % 2 == 0:
            results= gcdval
        else:
            results.append(gcdval + (K - 1) * lcmval)

    return results

# Read input
T = int(input())
test_cases = []

for _ in range(T):
    X, Y, K = map(int, input().split())
    test_cases.append((X, Y, K))

# Calculate and print the results
results = minimum_sum_after_operations(T, test_cases)
for result in results:
    print(result)
