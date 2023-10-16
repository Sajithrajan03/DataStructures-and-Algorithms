class heap:
    def __init__(self):
        self.heap = [ ]
    def heapify(self,i):
        heap_size = len(self.heap)
        largest = 0
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2

        if left_child_index < heap_size and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index

        if right_child_index < heap_size and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify(largest)
    def heap_sort(self):
        for i in range(len(self.heap)//2,-1,-1):
            self.heapify(i)
h = heap()
import random
a = [(random.randrange(1,20)) for _ in range(0,10)]
print(a)
h.heap = a
h.heap_sort()
print(h.heap)
