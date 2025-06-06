# Date: 2025-04-15
# Author: Sparsha Srinath
# Leetcode (Combination Sum III): https://leetcode.com/problems/combination-sum-iii/
# Tags: Backtracking, DFS

from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        Find all possible combinations of k numbers that add up to a number n,
        given that only numbers from 1 to 9 can be used and each combination should be a unique set.

        Args:
            k (int): Number of elements to choose.
            n (int): Target sum.

        Returns:
            List[List[int]]: List of all valid combinations.
        """

        nums = [i for i in range(1, 10)]  # Available digits from 1 to 9
        res = []
        cur = []

        def dfs(idx: int, total: int) -> None:
            if len(cur) == k and total == n:
                res.append(cur.copy())
                return

            if total > n:
                return

            for i in range(idx, len(nums)):
                cur.append(nums[i])             # Choose
                dfs(i + 1, total + nums[i])     # Explore with next index
                cur.pop()                       # Un-choose (backtrack)

        dfs(0, 0)
        return res
