# Date: 2025-05-28
# Author: Sparsha Srinath
# Leetcode (Matchsticks to Square): https://leetcode.com/problems/matchsticks-to-square/
# Tags: Backtracking, DFS, Bitmask, Pruning

from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        Determines if the given matchsticks can form a square.

        Args:
            matchsticks (List[int]): A list of integers representing matchstick lengths.

        Returns:
            bool: True if it's possible to form a square, False otherwise.
        """

        total = sum(matchsticks)
        
        # Early check: if total is not divisible by 4, can't form a square
        if total % 4 != 0:
            return False

        side_length = total // 4
        sides = [0] * 4

        # Sort matchsticks in descending order for better pruning
        matchsticks.sort(reverse=True)

        def dfs(index: int) -> bool:
            # Base case: all matchsticks have been placed
            if index == len(matchsticks):
                return all(side == side_length for side in sides)
            
            # Try placing the current matchstick in each of the 4 sides
            for i in range(4):
                if sides[i] + matchsticks[index] <= side_length:
                    sides[i] += matchsticks[index]
                    if dfs(index + 1):
                        return True
                    sides[i] -= matchsticks[index]  # Backtrack
                
                # Optimization: if one side is still 0 after trying, no need to try other empty sides
                if sides[i] == 0:
                    break

            return False

        return dfs(0)
