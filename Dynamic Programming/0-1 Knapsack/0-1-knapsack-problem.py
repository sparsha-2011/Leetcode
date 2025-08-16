# Author: Sparsha Srinath
# Date: 2025-08-16
# Problem: 0/1 Knapsack
# Link: https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1
# Tags: Dynamic Programming, Knapsack, DP-Table, Optimization
# Time Complexity: O(N * W)  # N = number of items, W = capacity of knapsack
# Space Complexity: O(N * W) (can be optimized to O(W))

from typing import List

class Solution:
    def knapSack(self, W: int, wt: List[int], val: List[int], n: int) -> int:
        """
        Function to return the maximum value that can be put in a knapsack of capacity W.
        Uses bottom-up DP (tabulation).
        """
        # DP table initialization
        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

        # Build table dp[][] in bottom-up manner
        for i in range(1, n + 1):
            for w in range(1, W + 1):
                if wt[i - 1] <= w:
                    dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
                else:
                    dp[i][w] = dp[i - 1][w]

        return dp[n][W]



    print("Maximum value in Knapsack =", obj.knapSack(W, wt, val, n))
