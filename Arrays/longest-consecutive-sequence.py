# Problem Title: Longest Consecutive Sequence
# Problem URL: https://leetcode.com/problems/longest-consecutive-sequence/
# Difficulty: Medium

"""
Problem Statement:

Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7

Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list to a set for O(1) lookups
        numSet = set(nums)
        longest = 0

        # Iterate through each number in the set
        for num in numSet:
            # Start a new sequence if the previous number is not in the set
            length = 1
            if (num - 1) not in numSet:
                # Check for consecutive numbers starting from `num`
                while (num + length) in numSet:
                    length += 1

            # Update the longest sequence found
            longest = max(longest, length)

        return longest
