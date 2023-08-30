import random
a = [(random.randrange(1,20)) for _ in range(0,10)]
n = len(a)

for i in range(1,n):
    key = a[i]
    j = i-1
    while(a[j] > key and j>=0):
        a[j+1] = a[j]
    
        j -= 1

    a[j+1] = key
print(a)
