import random as r
a = [r.randrange(0,20) for _ in range(20)]
for i in range(len(a)):
    min = i
    for j in range(i+1,len(a)):
        if a[min]>a[j]:
            min = j
    a[min] ,a[i] = a[i],a[min]
print(a)
