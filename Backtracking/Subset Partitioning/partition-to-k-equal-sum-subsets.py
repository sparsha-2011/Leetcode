# Author: Sparsha Srinath
# Date: 2025-08-13
# Problem: Partition to K Equal Sum Subsets
# Link: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# Tags: Backtracking, DFS, Sorting, Pruning
# Time Complexity: Exponential (O(k^n) in worst case, heavily pruned)
# Space Complexity: O(k + n) for buckets and recursion stack

from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    
        total = sum(nums)

        if total % k != 0:
            return False
        
        target = total // k
        buckets = [0] * k
        nums.sort(reverse=True)

        def backtrack(i):
            if i == len(nums):
                return True
            
            for b in range(k):
                if buckets[b] + nums[i] <= target:
                    buckets[b] += nums[i]
                    if backtrack(i + 1):
                        return True
                    buckets[b] -= nums[i]

                if buckets[b] == 0:
                    break
            return False

        return backtrack(0)
