"""
heap_implementations.py

This file demonstrates how to implement both Min Heap and Max Heap in Python using the built-in heapq module.
heapq is a binary heap implementation with O(log n) push and pop operations.
By default, heapq implements a Min Heap.

Author: Your Name
Date: YYYY-MM-DD
"""

import heapq

# ------------------------------
# MIN HEAP IMPLEMENTATION
# ------------------------------
class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        """Push value onto the heap"""
        heapq.heappush(self.heap, val)

    def pop(self):
        """Pop and return the smallest value from the heap"""
        return heapq.heappop(self.heap)

    def peek(self):
        """Return the smallest value without removing it"""
        return self.heap[0] if self.heap else None

    def __str__(self):
        return str(self.heap)


# ------------------------------
# MAX HEAP IMPLEMENTATION
# ------------------------------
class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        """Push value onto the max heap by inverting the value"""
        heapq.heappush(self.heap, -val)

    def pop(self):
        """Pop and return the largest value (inverted back)"""
        return -heapq.heappop(self.heap)

    def peek(self):
        """Return the largest value without removing it"""
        return -self.heap[0] if self.heap else None

    def __str__(self):
        """Return heap as a list of actual values (not inverted)"""
        return str([-x for x in self.heap])


# ------------------------------
# EXAMPLE USAGE
# ------------------------------
if __name__ == "__main__":
    print("=== Min Heap Demo ===")
    min_heap = MinHeap()
    for num in [5, 1, 3, 4]:
        min_heap.push(num)
    print("Heap:", min_heap)
    print("Pop:", min_heap.pop())
    print("Peek:", min_heap.peek())

    print("\n=== Max Heap Demo ===")
    max_heap = MaxHeap()
    for num in [5, 1, 3, 4]:
        max_heap.push(num)
    print("Heap:", max_heap)
    print("Pop:", max_heap.pop())
    print("Peek:", max_heap.peek())
