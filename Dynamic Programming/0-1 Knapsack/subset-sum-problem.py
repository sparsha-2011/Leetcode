# Author: Sparsha Srinath
# Date: 2025-08-16
# Problem: Subset Sum Problem
# Link: https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1
# Tags: Dynamic Programming, Subset Sum, 2D DP
# Time Complexity: O(n * sum)
# Space Complexity: O(n * sum)

class Solution:
    def isSubsetSum(self, arr, sum):
        """
        Determines if there exists a subset of the array with the given sum.

        Parameters:
            arr (List[int]): The input array
            sum (int): The target sum

        Returns:
            bool: True if a subset with the given sum exists, False otherwise
        """
        n = len(arr)

        # Initialize DP table
        dp = [[False] * (sum + 1) for _ in range(n + 1)]

        # Base case: sum 0 is always possible
        for i in range(n + 1):
            dp[i][0] = True

        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, sum + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][sum]
