# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Date: 2025-06-15
# Tags: heap, priority-queue, data-stream, kth-largest
#
# Description:
#   Design a class that finds the kth largest element in a stream of integers, including duplicates.
#   The kth largest element is the kth largest in sorted order, not necessarily a distinct value.
#
#   The approach:
#     - Use a min-heap of size k to maintain the k largest elements seen so far.
#     - On each insertion (add), push the new value and pop the smallest if the heap exceeds k.
#     - The root of the min-heap is always the kth largest element.
#
# Input:
#   k: int — the "k" in kth largest
#   nums: List[int] — initial stream of integers
#   val: int — new value added to the stream via add()
# Output:
#   int — the kth largest element after each insertion
#
# Example:
#   k = 2, stream = [1, 2, 3, 3]
#   Output sequence: 1, 1, 2, 3
#
# Time Complexity: O(log k) per insertion
# Space Complexity: O(k)

import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        """
        Initializes the KthLargest object with integer k and the initial list of integers nums.
        Maintains a min-heap of size k.
        """
        self.k = k
        self.minHeap = []

        for n in nums:
            heapq.heappush(self.minHeap, n)
            if len(self.minHeap) > self.k:
                heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        """
        Adds a new integer val to the stream and returns the kth largest element.
        """
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# ---------------------------
# Example usage / test block
# ---------------------------
if __name__ == "__main__":
    k = 2
    stream = [1, 2, 3, 3]
    kth = KthLargest(k, [])

    for num in stream:
        result = kth.add(num)
        print(f"After adding {num}, {k}th largest is: {result}")
