# Author: Sparsha Srinath
# Date: 2025-06-29
# Leetcode: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
# Tags: Sliding Window, HashSet
# Time Complexity: O(n)
# Space Complexity: O(k)
# Description:
#   Find the maximum sum of any subarray of length `k` in which all elements are distinct.

from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        Computes the maximum sum of a subarray with length k where all elements are distinct.

        Args:
            nums (List[int]): The input list of integers.
            k (int): The length of subarray to check for distinct elements.

        Returns:
            int: The maximum sum of any valid subarray of length k.
        """
        start = 0
        max_sum = 0
        cur_sum = 0
        elements = set()

        for end in range(len(nums)):
            if nums[end] not in elements:
                cur_sum += nums[end]
                elements.add(nums[end])

                # When window size hits k
                if end - start + 1 == k:
                    if len(elements) == k:
                        max_sum = max(max_sum, cur_sum)

                    # Slide the window
                    cur_sum -= nums[start]
                    elements.remove(nums[start])
                    start += 1

            else:
                # Remove from left until duplicate is removed
                while nums[start] != nums[end]:
                    cur_sum -= nums[start]
                    elements.remove(nums[start])
                    start += 1
                start += 1  # skip the duplicate itself

        return max_sum
