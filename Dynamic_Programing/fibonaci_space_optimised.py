def fib(n):
    cur = 0
    pre2 = 0
    pre = 1
    for i in range(n):
        cur = pre + pre2
        pre2 = pre
        pre = cur
    return cur

print(fib(6))

    