# Date: 2025-04-15
# Author: Sparsha Srinath
# Leetcode (Combination Sum II): https://leetcode.com/problems/combination-sum-ii/
# Tags: Backtracking, DFS, Recursion, Sorting, Arrays

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations in candidates where the candidate numbers sum to the target.
        Each number in candidates may only be used once in the combination. The solution set must not contain duplicate combinations.

        Args:
            candidates (List[int]): List of candidate numbers (may contain duplicates).
            target (int): The target sum.

        Returns:
            List[List[int]]: List of all unique combinations that sum to target.
        """
        res = []  # Final result list
        cur = []  # Temporary list to store current combination
        candidates.sort()  # Sort to facilitate duplicate skipping

        def dfs(res: List[List[int]], cur: List[int], idx: int, total: int) -> None:
            """
            Recursive DFS helper function to build valid combinations.

            Args:
                res: List to store final combinations.
                cur: Current combination being built.
                idx: Current index in candidates.
                total: Sum of elements in the current combination.
            """
            if total == target:
                # Found a valid combination
                res.append(cur.copy())
                return
            elif total > target:
                # Exceeds target, prune the path
                return
            else:
                prev = -1  # Placeholder to track duplicates at the same recursive level
                for i in range(idx, len(candidates)):
                    if candidates[i] != prev:
                        # Avoid using the same number more than once at the same depth
                        cur.append(candidates[i])  # Choose current candidate
                        dfs(res, cur, i + 1, total + candidates[i])  # Recurse without reusing current index
                        cur.pop()  # Backtrack
                    prev = candidates[i]  # Update previous element tracker

        dfs(res, cur, 0, 0)
        return res
