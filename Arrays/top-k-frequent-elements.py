# Problem Title: Top K Frequent Elements
# Problem URL: https://leetcode.com/problems/top-k-frequent-elements/
# Difficulty: Medium

"""
Problem Statement:
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements within the array.
The test cases are generated such that the answer is always unique.

You may return the output in any order.

Examples:
1. Input: nums = [1,2,2,3,3,3], k = 2
   Output: [2,3]

2. Input: nums = [7,7], k = 1
   Output: [7]

Constraints:
- 1 <= nums.length <= 10^4
- -1000 <= nums[i] <= 1000
- 1 <= k <= number of distinct elements in nums
"""

from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the `k` most frequent elements in the input array.

        Args:
        nums (List[int]): List of integers.
        k (int): Number of most frequent elements to return.

        Returns:
        List[int]: List of `k` most frequent elements in any order.
        """
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        print(count)

        for n, c in count.items():
            freq[c].append(n)

        print(freq)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

# Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Example Test Case 1
    nums = [1, 2, 2, 3, 3, 3]
    k = 2
    print(sol.topKFrequent(nums, k))  # Output: [2, 3]

    # Example Test Case 2
    nums = [7, 7]
    k = 1
    print(sol.topKFrequent(nums, k))  # Output: [7]

    # Additional Test Case
    nums = [4, 4, 4, 5, 5, 6]
    k = 2
    print(sol.topKFrequent(nums, k))  # Output: [4, 5]
