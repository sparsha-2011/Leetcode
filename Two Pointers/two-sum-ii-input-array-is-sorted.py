# Author: Sparsha Srinath  
# Date: 2025-06-29  
# Problem: Two Sum II - Input Array Is Sorted  
# Source: Leetcode - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/  
# Tags: Two Pointers, Binary Search, Array  
# Time Complexity: O(n)  
# Space Complexity: O(1)

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1  # Two pointers at start and end

        while l < r:
            curr_sum = numbers[l] + numbers[r]

            if curr_sum > target:
                r -= 1  # Need a smaller sum, move right pointer left
            elif curr_sum < target:
                l += 1  # Need a larger sum, move left pointer right
            else:
                return [l + 1, r + 1]  # Return 1-based indices
