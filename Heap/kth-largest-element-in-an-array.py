# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Date: 2025-06-15
# Tags: heap, sorting, top-k, min-heap, arrays, priority-queue
#
# Description:
#   Given an unsorted array, find the kth largest element.
#   Note: This is the kth largest element in **sorted order**, not the kth distinct element.
#
#   Approach:
#     - Use a Min Heap of size k.
#     - Iterate through the array:
#         - Push each element to the heap.
#         - If heap size exceeds k, remove the smallest element.
#     - The root of the heap will be the kth largest element.
#
# Input:
#   nums: List[int] — unsorted list of integers
#   k: int — the k value
# Output:
#   int — the kth largest element
#
# Example:
#   Input : nums = [3,2,1,5,6,4], k = 2
#   Output: 5
#
# Time Complexity: O(n log k)
# Space Complexity: O(k)

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]


# -----------------------------
# Optional test case to run
# -----------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # Output: 5
