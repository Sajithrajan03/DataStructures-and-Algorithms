for i in range(0, 8):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0
    print(max_so_far)
 
# Driver function to check the above function
 
 
a = [-2, -3, 4, -1, -2, 1, 5, -3]
 
print "Maximum contiguous sum is", maxSubArraySum(a, len(a))