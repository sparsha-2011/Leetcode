# Author: Sparsha Srinath
# Date: 2025-08-16
# Problem: 0/1 Knapsack
# Link: https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1
# Tags: Dynamic Programming, Knapsack, Optimization
# Time Complexity: O(n * W)  # n = number of items, W = capacity
# Space Complexity: O(n * W)  # using a 2D DP table

class Solution:
    def knapsack(self, W, val, wt):
        """
        Solves the 0/1 Knapsack problem using bottom-up DP.

        Parameters:
            W (int): Maximum weight capacity of the knapsack
            val (List[int]): Values of items
            wt (List[int]): Weights of items

        Returns:
            int: Maximum value that can be obtained
        """
        n = len(val)

        # Initialize DP table (n+1) x (W+1)
        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

        # Build the DP table
        for i in range(1, n + 1):
            for j in range(1, W + 1):
                if wt[i - 1] <= j:
                    # Either include the item or exclude it
                    dp[i][j] = max(val[i - 1] + dp[i - 1][j - wt[i - 1]], 
                                   dp[i - 1][j])
                else:
                    # Exclude the item
                    dp[i][j] = dp[i - 1][j]

        return dp[n][W]
