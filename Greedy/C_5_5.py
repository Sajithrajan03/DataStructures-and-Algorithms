def number_of_guard(house, r, n):
    house.sort()
     
    num_of_guard = 0
 
    # for iterate all precious things
    i = 0
    while (i < n) :
 
        # count number of guard
        num_of_guard += 1
 
        # find the middle location
        loc = house[i] + r
 
        # traverse till middle location
        while (i < n and house[i] <= loc):
            i += 1
 
        
        # insert guard
        i -= 1
 
        
        loc = house[i] + r
 
        # traverse till last precious thing in range
       
        while (i < n and house[i] <= loc):
            i += 1
 
    # return the number of guard
    return num_of_guard
 

   
precious_things = [ 7, 2, 4, 6, 5, 9, 12, 11 ]
r = 2
n = len(precious_things)

print("LIST\t\t:",[x for x in range(min(precious_things),max(precious_things)+1)])
print("Precious things :  ",end="")
for i in range(min(precious_things),max(precious_things)+1):
    if i in precious_things:
        print(i,end=", ")
    else:
        print(" , ",end="")
print("]")
print(number_of_guard(precious_things, r, n))

