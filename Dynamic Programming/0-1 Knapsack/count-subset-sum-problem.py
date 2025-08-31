# Author: Sparsha Srinath
# Date: 2025-08-19
# Problem: Perfect Sum Problem (Count of Subsets with Given Sum)
# Link: https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1
# Tags: Dynamic Programming, Subset Sum, 2D DP
# Time Complexity: O(N * target)
# Space Complexity: O(N * target)

class Solution:
    def perfectSum(self, arr, target):
        n = len(arr)
        
        # dp[i][j] = number of subsets using first i elements that sum up to j
        dp = [[0] * (target + 1) for i in range(n + 1)]
        
        # Base case: There's exactly 1 way to get sum 0 (by taking empty subset)
        dp[0][0] = 1
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(target + 1):
                if arr[i - 1] <= j:
                    # Choice 1: include current element arr[i-1]
                    # Choice 2: exclude current element
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]
                else:
                    # Cannot include arr[i-1], only exclude
                    dp[i][j] = dp[i - 1][j]
        
        # Answer: number of subsets using all n elements that sum to target
        return dp[n][target]
