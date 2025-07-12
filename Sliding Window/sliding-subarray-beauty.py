# Author: Sparsha Srinath
# Date: 2025-06-29
# Leetcode: https://leetcode.com/problems/sliding-subarray-beauty/
# Tags: Sliding Window, Frequency Array, Greedy
# Time Complexity: O(n * 50) → effectively O(n)
# Space Complexity: O(1) → because the frequency array size is constant
#
# Description:
#   For each subarray of size k, find the x-th smallest negative number.
#   If there are fewer than x negative numbers, return 0 for that subarray.
#   Efficiently done using a frequency array of negative numbers from -1 to -50.

from typing import List

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        freq = [0] * 51  # freq[1] to freq[50] represent -1 to -50
        result = []
        start = 0

        for end in range(len(nums)):
            if nums[end] < 0:
                freq[-nums[end]] += 1

            if end - start + 1 == k:
                count = 0
                neg_val = 0
                for val in range(50, 0, -1):
                    count += freq[val]
                    if count >= x:
                        neg_val = -val
                        break

                result.append(neg_val)

                if nums[start] < 0:
                    freq[-nums[start]] -= 1

                start += 1

        return result
