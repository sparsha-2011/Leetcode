# Problem: Split Array Largest Sum
# Link: https://leetcode.com/problems/split-array-largest-sum/
# Author: Sparsha Srinath
# Date: 2025-08-13
#
# Description:
# Given an array nums and an integer k, split the array into k non-empty subarrays
# to minimize the largest sum among these subarrays.
# 
# This is equivalent to the Allocate Minimum Pages problem, solved with binary search
# over the answer (search space = [max(nums), sum(nums)]).

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        # Helper: check if we can split nums into <= k subarrays with max sum <= limit
        def canSplit(limit: int) -> bool:
            subarrays = 1
            curr_sum = 0

            for num in nums:
                if curr_sum + num > limit:
                    subarrays += 1
                    curr_sum = num
                    if subarrays > k:
                        return False
                else:
                    curr_sum += num
            return True

        # Binary search range: max(nums) (min possible limit) to sum(nums) (max possible limit)
        low, high = max(nums), sum(nums)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if canSplit(mid):
                ans = mid
                high = mid - 1  # Try for a smaller limit
            else:
                low = mid + 1  # Need a larger limit
        
        return ans
