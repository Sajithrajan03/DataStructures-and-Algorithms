import random
a = [(random.randrange(1,20)) for _ in range(0,10)]
n = len(a)
iter = 0
for _ in range(0,n-1):
    for i in range(0,n-1):
        iter +=1
        if a[i]>a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]

    
print(a,iter)
