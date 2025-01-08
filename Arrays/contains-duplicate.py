# Problem Title: Contains Duplicate
# Problem URL: https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy

"""
Problem Statement:
Given an integer array `nums`, return `true` if any value appears more than once in the array, 
and `false` if every element is distinct.

Examples:
1. Input: nums = [1, 2, 3, 3]
   Output: true

2. Input: nums = [1, 2, 3, 4]
   Output: false

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Checks if there are duplicate values in the array.

        Args:
        nums (List[int]): The input array.

        Returns:
        bool: True if duplicates exist, False otherwise.
        """
        hash_set = set()  # Using a set for efficient lookups

        for i in nums:
            if i in hash_set:
                return True
            hash_set.add(i)
        
        return False
