# Date: 2025-04-15
# Author: Sparsha Srinath
# Leetcode (Subsets): https://leetcode.com/problems/subsets/
# Tags: Backtracking, DFS, Recursion, Bitmasking (alternative approach)

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible subsets (the power set) of a list of distinct integers.

        Args:
            nums (List[int]): The list of distinct integers.

        Returns:
            List[List[int]]: A list of all subsets.
        """
        res = []  # Final result list to hold all subsets
        cur = []  # Temporary list to build current subset

        def dfs(res: List[List[int]], cur: List[int], idx: int) -> None:
            """
            Depth-first search to explore all combinations starting from index `idx`.

            Args:
                res: The list to collect all subsets.
                cur: The current subset being built.
                idx: The current index in the original list.
            """
            # Print current subset and the result list at each recursive call (debugging)
            print(cur, res)

            # Add a copy of the current subset to the result
            res.append(cur.copy())

            # Iterate through the elements starting from `idx`
            for i in range(idx, len(nums)):
                cur.append(nums[i])         # Include nums[i] in the current subset
                dfs(res, cur, i + 1)        # Recurse to include further elements
                cur.pop()                   # Backtrack to explore other combinations

        dfs(res, cur, 0)
        return res

