# Date: 2025-04-15
# Author: Sparsha Srinath
# Leetcode (Permutations II): https://leetcode.com/problems/permutations-ii/
# Tags: Backtracking, DFS, Permutations

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Return all unique permutations of the input list `nums` that may contain duplicates.

        Args:
            nums (List[int]): List of integers (may contain duplicates)

        Returns:
            List[List[int]]: List of all unique permutations
        """
        nums.sort()  # Sort to easily skip duplicates
        used = [False] * len(nums)
        res = []
        cur = []

        def dfs():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                # Skip used elements
                if used[i]:
                    continue
                # Skip duplicates: only use the first un-used duplicate in a sequence
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                # Choose
                used[i] = True
                cur.append(nums[i])

                # Explore
                dfs()

                # Un-choose (backtrack)
                used[i] = False
                cur.pop()

        dfs()
        return res
