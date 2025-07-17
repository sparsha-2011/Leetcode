# Author: Sparsha Srinath  
# Date: 2025-06-29  
# Problem: 3Sum  
# Source: Leetcode - https://leetcode.com/problems/3sum/  
# Tags: Two Pointers, Sorting, Array  
# Time Complexity: O(n^2)  
# Space Complexity: O(1) (excluding output list)

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to use two-pointer technique
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break  # No three numbers can sum to zero beyond this point

            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for the first element

            l, r = i + 1, len(nums) - 1

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                if three_sum < 0:
                    l += 1  # Need a larger sum
                elif three_sum > 0:
                    r -= 1  # Need a smaller sum
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
