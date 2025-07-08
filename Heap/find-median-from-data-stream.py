# Author: Sparsha Srinath
# Date: 2025-07-08
# Tags: data-structures, heap, median, algorithm
# LeetCode URL: https://leetcode.com/problems/find-median-from-data-stream/
#
# Description:
#   Implementation of MedianFinder using two heaps (min-heap and max-heap)
#   Supports adding numbers from a data stream and finding the median efficiently.

import heapq

class MedianFinder:
    """
    Data structure to efficiently find the median in a stream of numbers.
    Uses two heaps:
      - maxHeap (as a negated min-heap) to store smaller half
      - minHeap to store larger half
    Balances heaps sizes to ensure median calculation in O(1) time.
    """

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        # Balance the heaps sizes
        while abs(len(self.minHeap) - len(self.maxHeap)) > 1:
            if len(self.minHeap) > len(self.maxHeap):
                val = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -val)
            else:
                val = -heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, val)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            return float(self.minHeap[0])
        else:
            return float(-self.maxHeap[0])
