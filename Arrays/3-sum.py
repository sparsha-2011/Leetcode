# Problem Title: 3Sum
# Problem URL: https://leetcode.com/problems/3sum/
# Difficulty: Medium

"""
Problem Statement:

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j, and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize the result list
        res = []
        # Sort the array to help with the two-pointer approach
        nums.sort()
        
        # Iterate through the sorted array
        for i, a in enumerate(nums):
            # Skip duplicate elements to avoid duplicate triplets
            if i > 0 and nums[i-1] == a:
                continue
            
            # Initialize two pointers: one after the current element and one at the end
            l, r = i + 1, len(nums) - 1

            # Use two-pointer approach to find the other two elements that sum to zero
            while l < r:
                threeSum = a + nums[l] + nums[r]

                # If the sum is greater than 0, move the right pointer left
                if threeSum > 0:
                    r -= 1
                # If the sum is less than 0, move the left pointer right
                elif threeSum < 0:
                    l += 1
                # If the sum is exactly 0, add the triplet to the result list
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # Skip duplicate elements on the left side
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
        return res
