# Date: 2025-04-15
# Author: Sparsha Srinath
# Leetcode (Subsets II): https://leetcode.com/problems/subsets-ii/
# Tags: Backtracking, DFS, Recursion, Sorting

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible subsets (the power set) of a list of integers,
        ensuring that there are no duplicate subsets.

        Args:
            nums (List[int]): The list of integers which may contain duplicates.

        Returns:
            List[List[int]]: A list of all unique subsets.
        """

        res = []        # Final result to store subsets
        cur = []        # Temporary list to build each subset
        nums.sort()     # Sort to handle duplicates

        def dfs(idx: int):
            """
            Depth-first search to generate subsets from index `idx`.

            Args:
                res: Main result list.
                cur: Current subset being built.
                idx: Current index in nums being considered.
            """
            res.append(cur.copy())  # Add the current subset to the result

            prev = None  # To track previous number and avoid duplicates
            for i in range(idx, len(nums)):
                if nums[i] != prev:  # Skip duplicates at the same depth
                    cur.append(nums[i])          # Include nums[i] in the current subset
                    dfs(i + 1)         # Recurse for the next elements
                    cur.pop()                    # Backtrack
                prev = nums[i]                   # Update previous

        dfs(0)
        return res



#Approach 2
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        nums.sort()

        def dfs(idx):
            res.append(cur.copy())

            for i in range(idx,len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                cur.append(nums[i])         # Include nums[i] in the current subset
                dfs(i + 1)        # Recurse to include further elements
                cur.pop()                   # Backtrack to explore other combinations

        dfs(0)
        return res
