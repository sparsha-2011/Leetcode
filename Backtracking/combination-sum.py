# Date: 2025-04-15
# Author: Sparsha Srinath
# Leetcode (Combination Sum): https://leetcode.com/problems/combination-sum/
# Tags: Backtracking, DFS, Recursion, Arrays

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations of candidates where the chosen numbers sum to the target.
        A number in candidates may be chosen unlimited times.

        Args:
            candidates (List[int]): List of distinct positive integers.
            target (int): The target sum.

        Returns:
            List[List[int]]: List of all unique combinations that sum to target.
        """
        res = []  # Final result list to store combinations
        cur = []  # Temporary list to build current combination

        def dfs(res: List[List[int]], cur: List[int], idx: int, total: int) -> None:
            """
            Recursive DFS helper to find valid combinations.

            Args:
                res: The final result list.
                cur: The current combination being built.
                idx: Current index in candidates.
                total: Current sum of elements in cur.
            """
            if total == target:
                # If current combination matches the target, add a copy to result
                res.append(cur.copy())
                return
            elif total > target:
                # If total exceeds target, stop exploring this path
                return
            else:
                # Explore all candidates starting from current index (allows reuse)
                for i in range(idx, len(candidates)):
                    cur.append(candidates[i])                 # Choose candidate
                    dfs(res, cur, i, total + candidates[i])   # Recurse with updated total
                    cur.pop()                                 # Backtrack

        dfs(res, cur, 0, 0)
        return res
