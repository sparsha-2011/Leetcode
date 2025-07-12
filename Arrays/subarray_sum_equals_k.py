# Author: Sparsha Srinath
# Date: 2025-06-29
# Leetcode: https://leetcode.com/problems/subarray-sum-equals-k/
# Tags: Prefix Sum, HashMap
# Time Complexity: O(n)
# Space Complexity: O(n)
# Description:
#   Given an array of integers `nums` and an integer `k`, return the total number of subarrays
#   whose sum equals to `k`.

from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Counts the number of continuous subarrays whose sum equals to k.

        Args:
            nums (List[int]): The list of integers.
            k (int): The target subarray sum.

        Returns:
            int: The number of subarrays whose elements sum up to k.
        """
        count = 0
        curr_sum = 0
        freq = defaultdict(int)
        freq[0] = 1  # To handle subarrays starting from index 0

        for num in nums:
            curr_sum += num

            # Check if there is a prefix sum that when removed from curr_sum gives k
            if (curr_sum - k) in freq:
                count += freq[curr_sum - k]

            # Record the current prefix sum
            freq[curr_sum] += 1

        return count
