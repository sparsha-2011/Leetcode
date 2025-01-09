# Problem Title: Two Sum
# Problem URL: https://leetcode.com/problems/two-sum/
# Difficulty: Easy

"""
Problem Statement:
Given an array of integers `nums` and an integer `target`, return the indices `i` and `j` 
such that `nums[i] + nums[j] == target` and `i != j`.

You may assume that:
- Every input has exactly one pair of indices `i` and `j` that satisfy the condition.
- Return the answer with the smaller index first.

Examples:
1. Input: nums = [3,4,5,6], target = 7
   Output: [0,1]
   Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

2. Input: nums = [4,5,6], target = 10
   Output: [0,2]

3. Input: nums = [5,5], target = 10
   Output: [0,1]

Constraints:
- 2 <= nums.length <= 1000
- -10^7 <= nums[i] <= 10^7
- -10^7 <= target <= 10^7
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two indices such that nums[i] + nums[j] == target.

        Args:
        nums (List[int]): The input list of integers.
        target (int): The target sum.

        Returns:
        List[int]: Indices of the two numbers whose sum equals the target.
        """
        diff = {}
        for i in range(len(nums)):
            if target - nums[i] in diff:
                return [diff[target - nums[i]], i]
            diff[nums[i]] = i
        return []

# Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Example Test Case 1
    nums = [3, 4, 5, 6]
    target = 7
    print(sol.twoSum(nums, target))  # Output: [0, 1]

    # Example Test Case 2
    nums = [4, 5, 6]
    target = 10
    print(sol.twoSum(nums, target))  # Output: [0, 2]

    # Example Test Case 3
    nums = [5, 5]
    target = 10
    print(sol.twoSum(nums, target))  # Output: [0, 1]

    # Additional Test Case
    nums = [2, 7, 11, 15]
    target = 9
    print(sol.twoSum(nums, target))  # Output: [0, 1]
