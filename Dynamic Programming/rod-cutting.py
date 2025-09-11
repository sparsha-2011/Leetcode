# Author: Sparsha Srinath
# Date: 2025-08-19
# Problem: Rod Cutting
# Link: https://practice.geeksforgeeks.org/problems/rod-cutting0840/1
# Tags: Dynamic Programming, Unbounded Knapsack
# Time Complexity: O(N^2)   # N = length of the rod
# Space Complexity: O(N^2)  # DP table of size (N+1) x (N+1)

class Solution:
    def cutRod(self, price):
        n = len(price)  # rod length

        # dp[i][j] = max revenue using first i lengths to cut rod of length j
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        
        # lengths array: lengths available for cuts [1, 2, ..., n]
        lengths = [i + 1 for i in range(n)] 
        
        # Build the DP table
        for i in range(1, n + 1):        # iterate over available lengths
            for j in range(1, n + 1):    # iterate over rod lengths
                if lengths[i - 1] <= j:
                    # Choice 1: include this length and add its price
                    # Choice 2: skip this length
                    dp[i][j] = max(price[i - 1] + dp[i][j - lengths[i - 1]], 
                                   dp[i - 1][j])
                else:
                    # Can't cut with this length, so skip it
                    dp[i][j] = dp[i - 1][j]
        
        # Final answer: max revenue for rod of length n
        return dp[n][n]
