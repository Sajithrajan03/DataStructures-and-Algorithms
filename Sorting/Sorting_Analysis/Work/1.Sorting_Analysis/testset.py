import random
import unittest
def testset(arr2):
    input_sizes = [100, 500, 1000, 2000, 5000,10000]
    
    for size in input_sizes:
            arr = [random.randint(1, 100) for i in range(size)]
            arr2.append(arr)