# Date: 2025-04-15
# Author: Sparsha Srinath
# Leetcode (Permutations): https://leetcode.com/problems/permutations/
# Tags: Backtracking, DFS, Recursion, Arrays

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible permutations of a list of distinct integers.

        Args:
            nums (List[int]): The list of distinct integers.

        Returns:
            List[List[int]]: A list containing all possible permutations.
        """
        res = []       # Final result list to store all permutations
        cur = []       # Temporary list to build current permutation
        used = set()   # Set to track elements already used in current permutation

        def dfs(cur: List[int]) -> None:
            """
            Recursive DFS helper to build permutations.

            Args:
                cur: Current permutation being built.
            """
            # Base case: if the current permutation is complete
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            # Try each number that hasn't been used yet
            for i in range(len(nums)):
                if nums[i] not in used:
                    used.add(nums[i])       # Mark the number as used
                    cur.append(nums[i])     # Add number to current permutation
                    dfs(cur)                # Recurse
                    used.remove(nums[i])    # Backtrack: unmark the number
                    cur.pop()               # Remove number from current path

        dfs(cur)
        return res

##Approach 2
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        used = [False]*len(nums)
        res = []
        cur = []

        def dfs(cur):

            if len(cur) == len(nums):
                res.append(cur.copy())
            
            for i in range(len(nums)):
                if used[i]:
                    continue

                #if duplicates are present uncomment below code
                # if i >0 and nums[i]==nums[i-1] and not used[i-1]:
                #     continue
                
                used[i] = True
                cur.append(nums[i])
                dfs(cur)
                used[i] = False
                cur.pop()
                
        dfs(cur)
        return res
        
